let requestURL = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/data.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  const jsonObj = request.response;
  var desc = jsonObj['description'];
  var trad = jsonObj['traduction'];
  showDescript();
}

function showDescript() {
  document.getElementById('desc-git').innerHTML = desc;
  document.getElementById("desc-button").innerHTML = "<button onclick='showButton()' style='float: right;'>Traducir a Español</button>";
}	

function showTrad() {
  textTrad.innerHTML = jsonObj['traduction'];
  document.getElementById('desc-git').innerHTML = trad;
  document.getElementById("desc-button").innerHTML = "<button onclick='showDescript()' style='float: right;'>Traducir a Ingles</button>";
}
