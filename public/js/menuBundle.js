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
document.querySelectorAll('.cn-book-section-container').forEach(node => {
  // if(node.querySelector('.active') != null){
  //   node.setAttribute('class', '.cn-book-section-container expand')
  // }else{
  //   node.setAttribute('class', '.cn-book-section-container collapse')
  // }

  if(node.querySelector('.active') == null){
    node.setAttribute('class', '.cn-book-section-container collapse')
  }

  if(node.parentNode.querySelector('.active') != null){
    node.setAttribute('class', '.cn-book-section-container expand')
  }


  eleToggler = document.createElement('input')
  eleToggler.setAttribute('type', 'image')
  eleToggler.setAttribute('class', 'menuControl')
  eleToggler.setAttribute('src', "/icons/baseline-expand_more.svg")

  eleToggler.addEventListener('click', function(event){

    if(node.getAttribute('class') == '.cn-book-section-container collapse'){
      this.setAttribute('src', "/icons/baseline-expand_less.svg")
      node.setAttribute('class', '.cn-book-section-container expand')
    }else if(node.getAttribute('class') == '.cn-book-section-container expand'){
      node.setAttribute('class', '.cn-book-section-container collapse')
      this.setAttribute('src', "/icons/baseline-expand_more.svg")

    }
  })

  if(node.querySelector('a') == null){
    eleToggler.setAttribute('class', 'menuControl empty')
  }

  let par = node.parentNode
  let lnk = par.querySelector('a')
  if(par.tagName == 'LI'){
    lnk.insertAdjacentElement('afterbegin',eleToggler)
  }
})
