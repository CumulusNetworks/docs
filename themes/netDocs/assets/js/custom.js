$(document).ready(function() {
  
  document.querySelectorAll('h2').forEach(node => {
		// Create var with id
		var anchor = node.id;
		// Test if h2 has id
		if (anchor.length > 0) {
			// Create html link with class name and image       
			var a = document.createElement('a');
			a.className = ('anchor-link');
	  	a.innerHTML = "<img src=\"https://icons.cumulusnetworks.com/01-Interface-Essential/27-Link-Unlink/hyperlink-circle.svg\" width=\"13\" height=\"13\">";
	  	a.href = "#" + anchor;
	  	// Append the html link to the current h2
			node.append(a);
    }
	});

  // find all the svg elements under the div with class screen-layout and add the Click Event Listener to them
  // PS: do not add the EventListener to the a tag, since it causes the div to get the class of 'active'
  document.querySelectorAll('.screen-layout svg').forEach(node => {
  	// so when the svg element is clicked
  	// 1. get all the a tags under screen-layout
  	// 2. if the a tag contains the 'active' class, remove it
  	// 3. set the class of the event target (svg element) parentnode (a tag) to 'active' if it does not already have it 
  	//														(i.e. when selecting the same layout)
  	node.addEventListener('click', function(e) {
  		var anchors = document.querySelector('.screen-layout').getElementsByTagName('a');
  		for (i = 0; i < anchors.length; i++) {
  			// console.log('anchor.classList=' + anchors[i].classList);
  			if (anchors[i].classList.contains('active')){
  				anchors[i].classList.remove('active');
  				// console.log('removed active: ' + anchors[i].classList);
  			}
  		};
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
