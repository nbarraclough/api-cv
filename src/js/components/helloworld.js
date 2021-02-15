export default (text = "Hello, Webasdfsdpack!!") => {
  const element = document.createElement("h1");

  element.innerHTML = text;
  element.id="app"
  return element;
};
