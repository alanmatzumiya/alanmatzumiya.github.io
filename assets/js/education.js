
let urlFile = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
let requestThesis = new XMLHttpRequest();
requestThesis.open('GET', urlFile);
requestThesis.responseType = 'json';
requestThesis.send();

requestProjects.onload = function() {
  const jsonThesis = requestThesis.response;
  document.getElementById('author').innerHTML = jsonProjects['thesis'][1]['author'];
}
