const crypto = require('crypto');

const password1 = 'joe123';
const password2 = 'joe123';

const createHash = (password) => {
	return new Promise((resolve, reject) => {
		const salt = crypto.randomBytes(16);
			crypto.scrypt(password, salt, 64, (err, result) => {
				if (err) {
					reject(err);
				}
				resolve(result.toString('hex'));
			});
	});
}