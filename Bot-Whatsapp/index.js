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
    console.log('✅ Bot está pronto!');

    const groupName = 'Tcc'; // substitua pelo nome do grupo
    const stickerPath = './stickers/adm.webp';

    const sticker = await MessageMedia.fromFilePath(stickerPath);

    const chats = await client.getChats();
    const group = chats.find(chat => chat.isGroup && chat.name === groupName);

    if (!group) {
        console.log('❌ Grupo não encontrado.');
        return;
    }

    // Loop: envia a cada 2 segundos
    setInterval(() => {
        client.sendMessage(group.id._serialized, sticker, { sendMediaAsSticker: true });
        console.log('✅ Figurinha enviada como sticker!');
    }, 2000); // tempo em milissegundos
});

client.initialize();

