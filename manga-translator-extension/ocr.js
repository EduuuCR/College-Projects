async function runOCR(imageElement) {
  try {
    // Faz o download seguro da imagem como um blob
    const response = await fetch(imageElement.src, { mode: 'cors' });

    if (!response.ok) {
      throw new Error(`Erro ao baixar imagem: ${response.status}`);
    }

    const blob = await response.blob();
    const objectURL = URL.createObjectURL(blob);

    console.log("Executando OCR na imagem:", imageElement.src);

    const result = await Tesseract.recognize(
      objectURL,
      'jpn',
      {
        logger: m => console.log(`[OCR] ${m.status}: ${Math.round(m.progress * 100)}%`)
      }
    );

    URL.revokeObjectURL(objectURL); // Libera o recurso após uso

    return result.data.text;
  } catch (error) {
    if (error.message.includes('Failed to fetch')) {
      console.warn("A imagem pode não permitir CORS. OCR ignorado para:", imageElement.src);
    } else {
      console.error("Erro ao fazer OCR na imagem:", error);
    }
    return '';
  }
}

