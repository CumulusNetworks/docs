document.querySelectorAll('.cn-book-section-container').forEach(node => {
 
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


  let par = node.parentNode
  let lnk = par.querySelector('a')
  if(par.tagName == 'LI'){
    lnk.insertAdjacentElement('afterbegin',eleToggler)
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
      e.preventDefault()
    })
  }
});




