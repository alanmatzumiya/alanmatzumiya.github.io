let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/data.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  const descript = request.response;
  showDescript(descript);
}

function showDescript(jsonObj) {
  const textDesc = document.getElementById('desc-git');
  textDesc.innerHTML = jsonObj['description'];
  document.getElementById("desc-button").innerHTML = "<button onclick='tradButton(jsonObj)' style='float: right;'>Traducir a Español</button>";
}	

function tradButton(jsonObj) {
  document.getElementById("desc-button").innerHTML = "<button onclick='showDescript(jsonObj)' style='float: right;'>Traducir a Ingles</button>";
}
