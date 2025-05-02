// background.js

chrome.runtime.onInstalled.addListener(() => {
  console.log("[Manga Translator] Extensão instalada.");
});

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ['libs/tesseract.min.js', 'ocr.js', 'translator.js', 'content.js']
  });
  console.log("[Manga Translator] Script injetado na aba.");
});
