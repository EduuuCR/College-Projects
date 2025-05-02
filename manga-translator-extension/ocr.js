// ocr.js

async function extractTextFromImage(base64Image, lang = 'jpn') {
  try {
    const result = await Tesseract.recognize(base64Image, lang, {
      logger: m => console.log(`[OCR] ${m.status}: ${Math.round(m.progress * 100)}%`)
    });
    return result.data.text;
  } catch (error) {
    console.error('[OCR] Erro ao extrair texto:', error);
    return '';
  }
}
