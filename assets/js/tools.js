request.onload = function() {
  showDescript();
}

function showDescript() {
  let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/data.json';
  let request = new XMLHttpRequest();
  request.open('GET', requestURL);
  request.responseType = 'json';
  request.send();
  const jsonObj = request.response;
  const textDesc = document.getElementById('desc-git');
  textDesc.innerHTML = jsonObj['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='tradButton()' style='float: right;'>Traducir a Español</button>";
}	

function tradButton() {
  let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/data.json';
  let request = new XMLHttpRequest();
  request.open('GET', requestURL);
  request.responseType = 'json';
  request.send();
  const jsonObj = request.response;
  const textTrad = document.getElementById('desc-git');
  textTrad.innerHTML = jsonObj['traduction'];
  document.getElementById("desc-button").innerHTML = "<button onclick='showDescript()' style='float: right;'>Traducir a Ingles</button>";
}
