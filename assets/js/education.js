
let urlThesis = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/thesis.json';
let requestThesis = new XMLHttpRequest();
requestThesis.open('GET', urlThesis);
requestThesis.responseType = 'json';
requestThesis.send();

requestThesis.onload = function() {
  const jsonThesis = requestThesis.response;
  const textMath = jsonThesis['thesisMath'];
  document.getElementById('author').innerHTML = textMath['author'];
}
