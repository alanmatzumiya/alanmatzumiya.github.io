let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  const jsonObj = request.response;
  document.getElementById('desc-git').innerHTML = jsonObj['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showTrad()' style='float: right;'>Read in Spanish</button>";
}

function showDescript() {
  let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
  let request = new XMLHttpRequest();
  request.open('GET', requestURL);
  request.responseType = 'json';
  request.send();

  request.onload = function() {
  const jsonObj = request.response;
  document.getElementById('desc-git').innerHTML = jsonObj['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showTrad()' style='float: right;'>Read in Spanish</button>";
  }
}			

function showTrad() {
  let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/projects.json';
  let request = new XMLHttpRequest();
  request.open('GET', requestURL);
  request.responseType = 'json';
  request.send();

  request.onload = function() {
  const jsonObj = request.response;
  document.getElementById('desc-git').innerHTML = jsonObj['traduction'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showDescript()' style='float: right;'>Read in English</button>";
  }
}
