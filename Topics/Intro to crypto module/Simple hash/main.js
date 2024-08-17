const crypto = require('crypto');

const algo = 'blake2s256';
const message = 'No pain, no gain :)';
const encoding = 'base64';

const hashed =  crypto.createHash(algo).update(message).digest(encoding);
