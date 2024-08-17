const fs = require("node:fs");
const path = require("node:path");

const args = process.argv.slice(2);


try {
  args.forEach(arg => {
    const [command, value] = arg.split('=');

    switch (command) {
      case '--exist':
        const filePath = path.resolve(__dirname, value);

        if (fs.existsSync(filePath)) {
          console.log(`The file ${value} exists!`);
          console.log(value);
        } else {
          console.log(`File ${value} doesn't exist!`);
        }
        break;

      case '--create':
        const dirPath = path.resolve(__dirname, value);
        if (value.includes('/')) {
          fs.mkdirSync(dirPath, { recursive: true });
          console.log(`The folders ${value} were created!`);
        } else {
          fs.mkdirSync(dirPath, { recursive: true });
          console.log(`The folder ${value} was created!`);
        }
        break;

      case '--remove':
        const fullPath = path.resolve(__dirname, value);
        if (value.includes('/')) {
          fs.rmdirSync(fullPath, { recursive: true });
          console.log(`The folder ${value.split('/')[0]} in ${value.split('/')[1]} folder was deleted!`);
        } else if (!(fs.existsSync(fullPath) && fs.statSync(fullPath).isDirectory() && fs)) {
          console.log(`This ${value} folder doesn't exist!`);
        } else {
          fs.rmdirSync(fullPath, { recursive: true });
          console.log(`The folder ${value} was deleted!`);
        }
        break;

      default:
        console.log('Unknown command.');
    }
  });
} catch (error) {
  console.error(`An error occurred: ${error.message}`);
}
