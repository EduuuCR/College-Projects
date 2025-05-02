// popup/popup.js

document.getElementById('startBtn').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      files: ['libs/tesseract.min.js', 'ocr.js', 'translator.js', 'content.js']
    });
    document.getElementById('statusMsg').textContent = "Tradução ativada!";
  });
});
