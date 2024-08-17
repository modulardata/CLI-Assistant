const args = process.argv;

args.forEach((arg) => {
    if (arg.endsWith("=")) {
        console.log("It seems you forget to specify argument!");
    } else if (arg.startsWith("--")) {
        let elements = arg.slice(2).split("=");
        console.log(`${elements[0]}: ${elements[1] ? elements[1] : "true"}`);

    } else if (arg.startsWith("-")) {
        console.log(`${arg.slice(1)}: true`);
    }
});