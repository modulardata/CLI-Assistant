

// Construct the URL here
const protocol = 'https:';
const hostname = 'www.example.com';
const port = '443';
const pathname = '/mydocument';

// Constructed URL
const constructedURL = url.format({
  protocol,
  hostname,
  port,
  pathname
});