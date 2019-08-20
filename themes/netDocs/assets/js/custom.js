$(document).ready(function() {

	function addCopyLink(clipboard) {

		let markdown = document.querySelector(".markdown");
		let heading = markdown.querySelectorAll("h2");

		heading.forEach(function (elem) {

	  	var anchor = elem.id;
	  	var anchorLink = window.location.href + '#' + anchor;

		  // Test if h2 has id
		  if (anchor.length > 0) {

	      var span = document.createElement('span');
		  	span.className = ('clipboard');
		  	span.setAttribute('data-clipboard-text', anchorLink);
		  	span.innerHTML = "<img src=\"https://icons.cumulusnetworks.com/01-Interface-Essential/27-Link-Unlink/hyperlink-circle.svg\" width=\"13\" height=\"13\">";

			  	// Append the html link to the current h2
				elem.append(span);

				span.addEventListener('click', function () {
	        clipboard.writeText(span.getAttribute('data-clipboard-text')).then(function () {
	            span.blur();
	            span.setAttribute('aria-label', 'Link copied to clipboard!');
	            span.classList.add('tooltip');
	            setTimeout(function () {
	                span.removeAttribute('aria-label');
	                span.classList.remove('tooltip');
	            }, 2000);
	        }, function (error) {
	            span.blur();
	            span.setAttribute('aria-label', 'Error');
	            span.classList.add('tooltip');
	            setTimeout(function () {
	                span.removeAttribute('aria-label');
	                span.classList.remove('tooltip');
	            }, 2000);
	        });
	    	});
		  }
		});
	}

	if (navigator && navigator.clipboard) {
    addCopyLink(navigator.clipboard);
  } else {
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/clipboard-polyfill/2.7.0/clipboard-polyfill.promise.js';
    script.integrity = 'sha256-waClS2re9NUbXRsryKoof+F9qc1gjjIhc2eT7ZbIv94=';
    script.crossOrigin = 'anonymous';
    script.onload = function() {
        addCopyLink(clipboard);
    };
  
    document.body.appendChild(script);
  }
  

  // find all the svg elements under the div with class screen-layout and add the Click Event Listener to them
  // PS: do not add the EventListener to the a tag, since it causes the div to get the class of 'active'
  document.querySelectorAll('.screen-layout:not([style*="display:none"]):not([style*="display: none"]) svg').forEach(node => {
  // document.querySelectorAll('.screen-layout svg').forEach(node => {
  	// so when the svg element is clicked
  	// 1. get all the a tags under screen-layout
  	// 2. if the a tag contains the 'active' class, remove it
  	// 3. set the class of the event target (svg element) parentnode (a tag) to 'active' if it does not already have it 
  	//														(i.e. when selecting the same layout)
  	node.addEventListener('click', function(e) {
  		// var anchors = document.querySelector('.screen-layout').getElementsByTagName('a');
  		// for (i = 0; i < anchors.length; i++) {
  			// console.log('anchor.classList=' + anchors[i].classList);
  			// if (anchors[i].classList.contains('active')){
  			// 	anchors[i].classList.remove('active');
  			// 	console.log('removed active: ' + anchors[i].classList);
  			// }
  		// };
      document.querySelectorAll('.screen-layout a').forEach(anchor => {;
        // console.log('anchor.classList=' + anchor.classList);
        if (anchor.classList.contains('active')){
          anchor.classList.remove('active')
          // console.log('removed active ' + anchor.classList);
        }
      });
  		if (!e.target.parentNode.classList.contains('active')){
  			e.target.parentNode.classList.add('active');
  			// console.log('add active: ' + e.target.parentNode.classList);  			
  		}
  		var sbStatusClasses = ['default', 'hide-left', 'hide-right', 'hide-both'];
  		var mainTag = document.querySelector('main');
  		sbStatusClasses.forEach(function(classname) {
  			if (mainTag.classList.contains(classname)) {
  				mainTag.classList.remove(classname);
  			}
  		});
  		if (e.target.parentNode.classList.contains('sb-right')) {
  			mainTag.classList.add('hide-left');
  		} else if (e.target.parentNode.classList.contains('sb-left')) {
  			mainTag.classList.add('hide-right');
  		} else if (e.target.parentNode.classList.contains('no-sb')) {
  			mainTag.classList.add('hide-both');
  		} else {
  			mainTag.classList.add('default');
  		}
  		e.preventDefault();
  	});
  });

	document.querySelectorAll('#m-doc-search-box a').forEach(node => {	
		node.addEventListener('click', function(e) {
	  	e.preventDefault();
		document.getElementById('m-doc-search-box').classList.toggle('searchOpen');
	  });
	});

	document.addEventListener('keypress', function(e) {
	    if(e.which == 13 && $(".m-doc-search-input").is(":focus") && $(".m-doc-search-input").val().length ) {
	    	window.location.href = "/search/?q="+$(".m-doc-search-input").val().trim();
	    }
	});

});
