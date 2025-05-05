console.log("✅ content.js carregado!"); // Verifica se o script foi injetado

document.addEventListener('DOMContentLoaded', () => {
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'translateImages') {
      const images = document.querySelectorAll('img');
      console.log("🔍 Imagens encontradas:", images.length); // Loga a quantidade de imagens

      images.forEach(async (img, index) => {
        try {
          const text = await runOCR(img); // Usa a função do ocr.js
          if (text.trim()) {
            const div = document.createElement('div');
            div.className = 'translated-text';
            div.innerText = text;

            // Estilo da caixa de tradução
            img.parentElement.style.position = 'relative';
            div.style.position = 'absolute';
            div.style.top = '0';
            div.style.left = '0';
            div.style.backgroundColor = 'rgba(0, 0, 0, 0.6)';
            div.style.color = 'white';
            div.style.padding = '4px';
            div.style.fontSize = '14px';
            div.style.zIndex = '9999';
            div.style.maxWidth = '100%';
            div.style.wordBreak = 'break-word';

            img.parentElement.appendChild(div);
          }
        } catch (err) {
          console.error(`❌ Erro ao processar imagem ${index + 1}:`, err);
        }
      });
    }
  });
});
