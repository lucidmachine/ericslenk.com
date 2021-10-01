/** Responsive Menu **/
function toggleClass(element, className) {
  if (element.classList.contains(className)) {
    element.classList.remove(className);
  } else {
    element.classList.add(className);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  Array.from(document.getElementsByClassName('menutitle')).forEach(menuTitleElement => {
    menuTitleElement.addEventListener('click', () => {

      toggleClass(menuTitleElement, 'active');

      Array.from(document.getElementsByClassName('menu')).forEach(menuElement => {
        toggleClass(menuElement, 'open');
      })
    });
  });
});
