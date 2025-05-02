// content.js

const mangaImages = document.querySelectorAll('img');

mangaImages.forEach(async (img, index) => {
  try {
    // Ignora imagens muito pequenas (como ícones)
    if (img.naturalWidth < 100 || img.naturalHeight < 100) return;

    // Cria canvas e desenha a imagem nele
    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);

    // Converte para base64
    const base64 = canvas.toDataURL('image/png');

    // Extrai texto com OCR
    const extractedText = await extractTextFromImage(base64);
    console.log(`Texto extraído da imagem ${index}:`, extractedText);

    if (!extractedText.trim()) return;

    // Traduz o texto
    const translatedText = await translateTextToPortuguese(extractedText);
    console.log(`Tradução da imagem ${index}:`, translatedText);

    // Cria o overlay com a tradução
    const overlay = document.createElement('div');
    overlay.innerText = translatedText;
    overlay.className = 'translated-overlay';

    // Posiciona o overlay na mesma posição da imagem
    const rect = img.getBoundingClientRect();
    overlay.style.position = 'absolute';
    overlay.style.left = `${window.scrollX + rect.left}px`;
    overlay.style.top = `${window.scrollY + rect.top}px`;
    overlay.style.width = `${rect.width}px`;

    document.body.appendChild(overlay);
  } catch (err) {
    console.error(`Erro ao processar imagem ${index}:`, err);
  }
});
