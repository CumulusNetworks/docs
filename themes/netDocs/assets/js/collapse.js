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

  expand_more = '{{"icons/baseline-expand_more.svg" | absURL}}'
  eleToggler = document.createElement('input')
  eleToggler.setAttribute('type', 'image')
  eleToggler.setAttribute('class', 'menuControl')
  //$baseline-expand_more: '{{"icons/baseline-expand_more.svg" | absURL}}'
  eleToggler.setAttribute('src', expand_more)


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




