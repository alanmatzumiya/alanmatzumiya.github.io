
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
  document.getElementById('url-math').innerHTML = "<a href="+textMath['url']+" target='_blank'>Thesis Document</a>";
  document.getElementById('description-math').innerHTML = textMath['description'];
  document.getElementById('sponsorship-math').innerHTML = textMath['sponsorship'];
  document.getElementById('publisher-math').innerHTML = textMath['publisher'];
  document.getElementById('classification-math').innerHTML = textMath['classification'];
  document.getElementById('title-math').innerHTML = textMath['title'];
  document.getElementById('type-math').innerHTML = textMath['type'];
  const textChemistry = jsonThesis['thesisChemistry'];
  document.getElementById('author-chemistry').innerHTML = textChemistry['author'];
  document.getElementById('date-chemistry').innerHTML = textChemistry['date'];
  document.getElementById('url-chemistry').innerHTML = "<a href="+textChemistry['url']+" target='_blank'>Thesis Document</a>";
  document.getElementById('description-chemistry').innerHTML = textMath['description'];
  document.getElementById('sponsorship-chemistry').innerHTML = textChemistry['sponsorship'];
  document.getElementById('publisher-chemistry').innerHTML = textChemistry['publisher'];
  document.getElementById('classification-chemistry').innerHTML = textChemistry['classification'];
  document.getElementById('title-chemistry').innerHTML = textChemistry['title'];
  document.getElementById('type-chemistry').innerHTML = textChemistry['type'];
}
