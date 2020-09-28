let URL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
let requestProjects = new XMLHttpRequest();
requestProjects.open('GET', URL);
requestProjects.responseType = 'json';
requestProjects.send();

requestProjects.onload = function() {
  const jsonProjects = requestProjects.response;
  document.getElementById('desc-git').innerHTML = jsonProjects['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showTrad()' style='float: right;'>Read in Spanish</button>";
}

function showDescript() {
  let URL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
  let requestProjects = new XMLHttpRequest();
  requestProjects.open('GET', URL);
  requestProjects.responseType = 'json';
  requestProjects.send();

  requestProjects.onload = function() {
  const jsonProjects = requestProjects.response;
  document.getElementById('desc-git').innerHTML = jsonProjects['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showTrad()' style='float: right;'>Read in Spanish</button>";
  }
}			

function showTrad() {
  let URL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
  let requestProjects = new XMLHttpRequest();
  requestProjects.open('GET', URL);
  requestProjects.responseType = 'json';
  requestProjects.send();

  requestProjects.onload = function() {
  const jsonProjects = requestProjects.response;
  document.getElementById('desc-git').innerHTML = jsonProjects['traduction'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showDescript()' style='float: right;'>Read in English</button>";
  }
}
