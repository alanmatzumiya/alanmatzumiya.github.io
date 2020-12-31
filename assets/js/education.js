
let urlThesis = 'https://raw.githubusercontent.com/alanmatzumiya/alanmatzumiya.github.io/gh-pages/assets/thesis.json';
let requestThesis = new XMLHttpRequest();
requestThesis.open('GET', urlThesis);
requestThesis.responseType = 'json';
requestThesis.send();

requestThesis.onload = function() {
  const jsonThesis = requestThesis.response;
  const textMath = jsonThesis['thesisMath'];
  document.getElementById('author-math').innerHTML = textMath['author'];
  document.getElementById('date-math').innerHTML = textMath['date'];
  document.getElementById('url-math').innerHTML = "<a href="+textMath['url']+"Thesis"+"</a>";
  document.getElementById('description-math').innerHTML = textMath['description'];
  document.getElementById('sponsorship-math').innerHTML = textMath['sponsorship'];
  document.getElementById('publisher-math').innerHTML = textMath['publisher'];
  document.getElementById('classification-math').innerHTML = textMath['classification'];
  document.getElementById('title-math').innerHTML = textMath['title'];
  document.getElementById('type-math').innerHTML = textMath['type'];
}
