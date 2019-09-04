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
    var heading = document.querySelectorAll(".markdown h1, h2, h3, h4");
    var headings = {};
    var i = 0;

    Array.prototype.forEach.call(heading, function(e) {
      headings[e.id] = e.offsetTop;
    });
    
    if( document.querySelector('.book-toc') ) {
      document.querySelector('.book-toc #TableOfContents a:first-of-type').setAttribute('class', 'active');
    }

    window.onscroll = function() {
      var scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
    
      for (i in headings) {
        if (headings[i] <= scrollPosition) {
          // you're at the bottom of the page
          if ((window.innerHeight + scrollPosition) >= document.body.offsetHeight) {
            var group = [];
            var links =  document.querySelectorAll('.book-toc #TableOfContents a');

            links.forEach(link => {
              group.push(link);
            })

            document.querySelector('.book-toc #TableOfContents .active').setAttribute('class', ' ');
            group[group.length - 1].setAttribute('class', 'active')
           
          }else {
            document.querySelector('.book-toc #TableOfContents .active').setAttribute('class', ' ');
            document.querySelector('.book-toc #TableOfContents a[href*="#'+i+'"]').setAttribute('class', 'active')
          }

        }
      }
    };

  });
})()


