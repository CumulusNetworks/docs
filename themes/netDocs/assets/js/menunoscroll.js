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
    var elem = document.querySelectorAll('.dropdown');
    elem.forEach(dropdown => {
      if (dropdown.classList.contains('show')) dropdown.classList.remove('show');
    })
  }

  document.addEventListener('click', function(e) {
    var target = e.target;
    if (target.closest('.dropdown')){ 
      toggleDropdown(target); 
    }else {
      hideDropdown();
    }
  },false);

  document.addEventListener('DOMContentLoaded', function () {
    let markdown = document.querySelector(".markdown");
    let heading = markdown.querySelectorAll("h1, h2, h3, h4");
    let headings = {};
    let tocNav = document.querySelector('.book-toc');

    if (tocNav != null && tocNav.length > 0) {
      tocNav.querySelector('.book-toc nav a:first-of-type').setAttribute('class','active');
    }
    
    Array.prototype.forEach.call(heading, function(e) {
      headings[e.id] = e.offsetTop
    });


  });
})()


