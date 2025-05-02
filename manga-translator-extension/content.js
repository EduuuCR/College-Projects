// Seleciona todas as imagens da página
const mangaImages = document.querySelectorAll('img');

mangaImages.forEach(async (img, index) => {
  try {
    // Cria um canvas temporário
    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);

    // Converte para base64
    const base64 = canvas.toDataURL('image/png');

    // Executa OCR com Tesseract.js
    const result = await Tesseract.recognize(base64, 'jpn', {
      logger: m => console.log(`Img ${index}:`, m.status, m.progress)
    });

    const extractedText = result.data.text;
    console.log(`Texto extraído da imagem ${index}:`, extractedText);

    // Traduz texto para português
    const translatedText = await translateTextToPortuguese(extractedText);
    console.log(`Tradução da imagem ${index}:`, translatedText);

    // Exibe tradução sobre a imagem
    const overlay = document.createElement('div');
    overlay.innerText = translatedText;
    overlay.style.position = 'absolute';
    overlay.style.left = img.offsetLeft + 'px';
    overlay.style.top = img.offsetTop + 'px';
    overlay.style.background = 'rgba(0, 0, 0, 0.7)';
    overlay.style.color = 'white';
    overlay.style.padding = '4px';
    overlay.style.maxWidth = img.width + 'px';
    overlay.style.zIndex = 9999;
    overlay.style.fontSize = '14px';

    img.parentElement.appendChild(overlay);
  } catch (err) {
    console.error(`Erro ao processar imagem ${index}:`, err);
  }
});
