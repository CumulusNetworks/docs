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
