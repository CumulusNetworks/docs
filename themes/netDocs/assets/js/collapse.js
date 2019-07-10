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

  function load_url (url) {
    fetch(url)
    .then(function(response) {
        // When the page is loaded convert it to text
        return response.text()
    })
    .then(function(html) {
        // Initialize the DOM parser
        var parser = new DOMParser();

        // Parse the text
        var doc = parser.parseFromString(html, "text/html");
        var content = doc.querySelector(".markdown").innerHTML;
        document.querySelector(".markdown").innerHTML = content;
    })
    .catch(function(err) {  
        console.log('Failed to fetch page: ', err);  
    });
} 


  let par = node.parentNode
  let lnk = par.querySelector('a')

  if(par.tagName == 'LI'){
    lnk.insertAdjacentElement('afterbegin',eleToggler)
    lnk.addEventListener('click', function (e) {
      let url = lnk.getAttribute("href");

      if (lnk.classList.contains('active')) {
        lnk.classList.remove('active')
        lnk.nextElementSibling.classList.remove('expand')
        lnk.nextElementSibling.classList.add('collapse')
      }else {
        lnk.classList.add('active')
        lnk.nextElementSibling.classList.remove('collapse')
        lnk.nextElementSibling.classList.add('expand')
      }
      load_url(url)
      e.preventDefault()
    })
  }
});




