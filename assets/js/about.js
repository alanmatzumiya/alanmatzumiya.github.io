let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/about.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  const jsonObj = request.response;
  const textAbout = jsonObj['about']; 
  document.getElementById('resumen').innerHTML = textAbout['resumen'];
  document.getElementById('content').innerHTML = textAbout['content'];
  document.getElementById('something-else').innerHTML = textAbout['something-else'][0] + '<br><br>' + textAbout['something-else'][1] + '<br><br>' + textAbout['something-else'][2] + '<br><br>' + textAbout['something-else'][3];
}
