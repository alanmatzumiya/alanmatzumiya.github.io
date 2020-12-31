let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/about.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  const jsonObj = request.response;
  const textAbout = jsonObj['about']; 
  document.getElementById('motivation').innerHTML = textAbout['motivation'];
  document.getElementById('content').innerHTML = textAbout['content'];
  document.getElementById('commentary').innerHTML = textAbout['commentary'][0] + '<br><br>' + textAbout['commentary'][1] + '<br><br>' + textAbout['commentary'][2] + '<br><br>' + textAbout['commentary'][3];
}
