<?php
if (isset($_GET['code']) && !empty(trim($_GET['code']))) {
    $short_code = trim($_GET['code']);

    $db_path = __DIR__ . '/database/shortener.sqlite';

    if (!file_exists($db_path)) {
        die("Database not found. Please run index.php first to create it.");
    }

    try {
        $db = new PDO('sqlite:' . $db_path);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Prepare statement to find the long URL and update hits
        $stmt = $db->prepare("SELECT long_url FROM urls WHERE short_code = :short_code");
        $stmt->bindParam(':short_code', $short_code);
        $stmt->execute();

        $result = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($result && isset($result['long_url'])) {
            // Increment hits count
            $updateStmt = $db->prepare("UPDATE urls SET hits = hits + 1 WHERE short_code = :short_code");
            $updateStmt->bindParam(':short_code', $short_code);
            $updateStmt->execute();

            // Redirect to the long URL
            header("Location: " . $result['long_url'], true, 301); // 301 for permanent redirect
            exit;
        } else {
            http_response_code(404);
            die("Short URL not found.");
        }
    } catch (PDOException $e) {
        http_response_code(500);
        die("Database error: " . $e->getMessage());
    }
} else {
    http_response_code(400);
    die("No short code provided.");
}
?>
