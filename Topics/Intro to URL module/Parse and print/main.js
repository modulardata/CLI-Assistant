const urlString = "https://jsonplaceholder.typicode.com/posts";

const urlObject = new URL(urlString);
const arrayOfPath = urlObject.pathname.split("/");