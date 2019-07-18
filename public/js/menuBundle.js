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

    tocNav.querySelector('.book-toc nav a:first-of-type').setAttribute('class','active');
    
    Array.prototype.forEach.call(heading, function(e) {
      headings[e.id] = e.offsetTop
    });

    window.onscroll = function() {
      let scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
      let i = 0;
      for (i in headings) {
        if (headings[i] <= scrollPosition - 230 && headings[i] !== 0) {
          tocNav.querySelectorAll('a').forEach(node => {
            node.setAttribute('class', '');
          })
          tocNav.querySelector('.book-toc nav a[href="#'+i+'"]').setAttribute('class','active');
        }
      }
    };
  });
})()
document.querySelectorAll('.cn-book-section-container').forEach(node => {
 
  if(node.querySelector('.active') == null){
    node.setAttribute('class', '.cn-book-section-container collapse')
  }
  if(node.parentNode.querySelector('.active') != null){
    if(node.parentNode.tagName == 'LI'){
      node.parentNode.querySelector('a').setAttribute('class', 'active')
    }
    node.setAttribute('class', '.cn-book-section-container expand')
  }

  eleToggler = document.createElement('input')
  eleToggler.setAttribute('type', 'image')
  eleToggler.setAttribute('class', 'menuControl')
  eleToggler.setAttribute('src', "/icons/baseline-expand_more.svg")


  let par = node.parentNode
  let lnk = par.querySelector('a')

  if(par.tagName == 'LI'){
    lnk.insertAdjacentElement('afterbegin',eleToggler)
    const toggler = lnk.querySelector('.menuControl');
    toggler.addEventListener('click', function(e) {
      e.preventDefault();
    });

    lnk.addEventListener('click', function (e) {
      if (lnk.classList.contains('active')) {
        lnk.classList.remove('active')
        lnk.nextElementSibling.classList.remove('expand')
        lnk.nextElementSibling.classList.add('collapse')
      }else {
        lnk.classList.add('active')
        lnk.nextElementSibling.classList.remove('collapse')
        lnk.nextElementSibling.classList.add('expand')
      }
    })
  }
});




