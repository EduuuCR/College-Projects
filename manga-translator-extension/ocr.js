import Tesseract from 'tesseract.js';

async function runOCR(imageElement) {
    console.log('Iniciando OCR com proxy CORS...');

    const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
    const imageUrl = imageElement.src;

    try {
        const response = await fetch(proxyUrl + imageUrl);
        const blob = await response.blob();
        const imageBitmap = await createImageBitmap(blob);

        const canvas = document.createElement('canvas');
        canvas.width = imageBitmap.width;
        canvas.height = imageBitmap.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(imageBitmap, 0, 0);

        const { data: { text } } = await Tesseract.recognize(
            canvas,
            'jpn',
            {
                logger: m => console.log(m),
            }
        );

        console.log("Texto reconhecido:", text);
        alert("Texto reconhecido:\n" + text);
    } catch (err) {
        console.error('Erro ao processar imagem para OCR:', err);
        alert('Erro ao processar imagem para OCR. Veja o console.');
    }
}

function traduzirImagens() {
    const imagens = document.querySelectorAll('img.page-img');
    if (imagens.length === 0) {
        console.warn('Nenhuma imagem de mangá encontrada na página.');
    } else {
        console.log(`Encontradas ${imagens.length} imagens de mangá. Iniciando OCR...`);
    }

    imagens.forEach((img, index) => {
        console.log(`Processando imagem ${index + 1}...`);
        runOCR(img);
    });
}

// Executa a função após o carregamento da página
window.addEventListener('load', () => {
    console.log("Script OCR carregado e rodando.");
    traduzirImagens();
});
