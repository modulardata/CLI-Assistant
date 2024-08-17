const decryptedMessages = [];
encryptedMessages.map(message => {
    const decipher = crypto.createDecipheriv(algorithm, key, iv);
    let decrypted = decipher.update(message, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    decryptedMessages.push(decrypted);
});
