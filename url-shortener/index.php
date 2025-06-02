<?php
session_start(); // To display messages

// Database connection
$db_path = __DIR__ . '/database/shortener.sqlite';
$db_dir = dirname($db_path);

if (!is_dir($db_dir)) {
    mkdir($db_dir, 0755, true);
}

try {
    $db = new PDO('sqlite:' . $db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Create table if it doesn't exist
    $db->exec("CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        long_url TEXT NOT NULL,
        short_code TEXT NOT NULL UNIQUE,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        hits INTEGER DEFAULT 0
    )");
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

function generateShortCode($length = 6) {
    // Characters to use for the short code
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

$short_url_display = '';
$error_message = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['long_url'])) {
    $long_url = trim($_POST['long_url']);

    // Validate URL
    if (empty($long_url)) {
        $error_message = "Please enter a URL.";
    } elseif (!filter_var($long_url, FILTER_VALIDATE_URL)) {
        $error_message = "Please enter a valid URL (e.g., http://example.com).";
    } else {
        try {
            // Check if URL already exists
            $stmt = $db->prepare("SELECT short_code FROM urls WHERE long_url = :long_url");
            $stmt->bindParam(':long_url', $long_url);
            $stmt->execute();
            $existing = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($existing) {
                $short_code = $existing['short_code'];
            } else {
                // Generate a unique short code
                do {
                    $short_code = generateShortCode();
                    $stmt = $db->prepare("SELECT id FROM urls WHERE short_code = :short_code");
                    $stmt->bindParam(':short_code', $short_code);
                    $stmt->execute();
                } while ($stmt->fetchColumn());

                // Insert new URL
                $stmt = $db->prepare("INSERT INTO urls (long_url, short_code) VALUES (:long_url, :short_code)");
                $stmt->bindParam(':long_url', $long_url);
                $stmt->bindParam(':short_code', $short_code);
                $stmt->execute();
            }

            // Construct the full short URL to display
            // This assumes redirect.php handles the short code directly in the query string
            // For cleaner URLs (like yoursite.com/shortcode), you'll need .htaccess
            $protocol = isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? "https" : "http";
            $host = $_SERVER['HTTP_HOST'];
            $base_dir = rtrim(dirname($_SERVER['PHP_SELF']), '/\\'); // Handles subdirectories

            // If using .htaccess for clean URLs (e.g., yoursite.com/shortcode)
            // $short_url_display = $protocol . '://' . $host . $base_dir . '/' . $short_code;

            // If using redirect.php?code=shortcode
            $short_url_display = $protocol . '://' . $host . $base_dir . '/redirect.php?code=' . $short_code;


            $_SESSION['success_message'] = "URL shortened successfully!";

        } catch (PDOException $e) {
            $error_message = "Error: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP URL Shortener</title>
    <link rel="stylesheet" href="style.css"> <style>
        /* Basic inline styles if style.css is not used */
        body { font-family: sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
        .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
        h1 { text-align: center; color: #333; }
        form { display: flex; flex-direction: column; gap: 10px; }
        input[type="url"], input[type="text"] { padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; }
        button { padding: 10px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #0056b3; }
        .message { padding: 10px; margin-top: 15px; border-radius: 4px; }
        .error { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .success { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .short-url-display { margin-top: 20px; padding: 10px; background-color: #e9ecef; border: 1px solid #ced4da; border-radius: 4px; }
        .short-url-display a { color: #007bff; text-decoration: none; font-weight: bold; }
        .short-url-display a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>PHP URL Shortener</h1>

        <?php if (isset($_SESSION['success_message']) && $short_url_display): ?>
            <div class="message success">
                <?php echo $_SESSION['success_message']; unset($_SESSION['success_message']); ?>
            </div>
            <div class="short-url-display">
                Shortened URL: <a href="<?php echo htmlspecialchars($short_url_display); ?>" target="_blank"><?php echo htmlspecialchars($short_url_display); ?></a>
                <br>
                (Copy this link)
            </div>
        <?php endif; ?>

        <?php if ($error_message): ?>
            <div class="message error"><?php echo htmlspecialchars($error_message); ?></div>
        <?php endif; ?>

        <form action="index.php" method="POST">
            <label for="long_url">Enter URL to shorten:</label>
            <input type="url" id="long_url" name="long_url" placeholder="https://www.example.com/very/long/url" required>
            <button type="submit">Shorten</button>
        </form>
    </div>
</body>
</html>
