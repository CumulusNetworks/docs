(function() {
  var menu = document.querySelector('aside.book-menu nav');
  addEventListener('beforeunload', function(event) {
    localStorage.setItem('menu.scrollTop', menu.scrollTop)
  });
  menu.scrollTop = localStorage.getItem('menu.scrollTop');

  var siteNav = document.getElementById('site-nav');
  var burgerMenu = document.querySelector('.burger-menu');
  burgerMenu.addEventListener('click', function() {
    siteNav.classList.toggle('menu-opened');
  });

  toggleDropdown = (elem) => {
    elem.parentNode.classList.toggle('show');
  }

  hideDropdown = () => {
    var elem = document.querySelector('.dropdown');
    if (elem.classList.contains('show')) elem.classList.remove('show');
  }

  document.addEventListener('click', function(e) {
    var target = e.target;
    if (target.closest('.dropdown')){ 
      toggleDropdown(target); 
    }else {
      hideDropdown();
    }
  },false);
})()
