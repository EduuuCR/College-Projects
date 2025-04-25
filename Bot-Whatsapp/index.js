const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const path = require('path');
const fs = require('fs');

const client = new Client({
    authStrategy: new LocalAuth()
});

client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', async () => {
    console.log('✅ Bot is ready!');

    const groupName = 'Tcc'; // replace with the group name
    const stickerPath = './stickers/adm.webp'; //replace with the sticker path

    const sticker = await MessageMedia.fromFilePath(stickerPath);

    const chats = await client.getChats();
    const group = chats.find(chat => chat.isGroup && chat.name === groupName);

    if (!group) {
        console.log('❌ Group not found.');
        return;
    }

   // Loop: sends every x seconds
    setInterval(() => {
        client.sendMessage(group.id._serialized, sticker, { sendMediaAsSticker: true });
        console.log('✅ Sticker has been sent!');
    }, 1500); // time in milliseconds
});

client.initialize();

