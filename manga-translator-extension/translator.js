// translator.js

async function translateTextToPortuguese(text) {
  try {
    const res = await fetch("https://translate.googleapis.com/translate_a/single?client=gtx&sl=ja&tl=pt&dt=t&q=" + encodeURIComponent(text));
    const data = await res.json();

    // Extrai apenas a string traduzida
    const translated = data[0].map(item => item[0]).join('');
    return translated;
  } catch (error) {
    console.error('[Tradução] Erro ao traduzir texto:', error);
    return '(Erro na tradução)';
  }
}
