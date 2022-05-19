let URL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
let requestProjects = new XMLHttpRequest();
requestProjects.open('GET', URL);
requestProjects.responseType = 'json';
requestProjects.send();

requestProjects.onload = function() {
  const jsonProjects = requestProjects.response;
  document.getElementById('desc-git').innerHTML = jsonProjects['description'];
}
