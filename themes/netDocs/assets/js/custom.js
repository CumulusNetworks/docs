$(document).ready(function() {

	function addCopyLink(clipboard) {

		let markdown = document.querySelector(".markdown");
		let heading = markdown.querySelectorAll("h2, h3, h4");

		heading.forEach(function (elem) {

	  	var anchor = elem.id;
      var anchorLink = location.href.replace(location.hash,"") + '#' + anchor;

		  // Test if h2 has id
		  if (anchor.length > 0) {

	      var span = document.createElement('span');
		  	span.className = ('clipboard');
		  	span.setAttribute('data-clipboard-text', anchorLink);
		  	span.innerHTML = "<img src=\"https://icons.cumulusnetworks.com/01-Interface-Essential/27-Link-Unlink/hyperlink-circle.svg\" width=\"13\" height=\"13\">";

			  // Append the html link to the current h2
				elem.append(span);

				span.addEventListener('click', function (e) {

          var historyState = {};

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

          var url = span.getAttribute('data-clipboard-text');
          history.pushState(null, null, url);

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
	
	// set local storage value to cache default layout on load
	if(window.localStorage.layout) {
		var mainTag = document.querySelector('main');

		document.querySelectorAll('.screen-layout a').forEach(anchor => {
			if (anchor.classList.contains('active')){
				anchor.classList.remove('active')
			}
			if(anchor.classList.contains(window.localStorage.trigger)) {
				anchor.classList.add('active')
			}
		});
		mainTag.classList.add(window.localStorage.layout)
	}else {
		var mainTag = document.querySelector('main');

		window.localStorage.setItem("trigger", "default");

		document.querySelectorAll('.screen-layout a').forEach(anchor => {
			if (anchor.classList.contains('active')){
				anchor.classList.remove('active')
			}
			if(anchor.classList.contains(window.localStorage.trigger)) {
				anchor.classList.add('active')
			}
		});

		window.localStorage.setItem("layout", "default");
		mainTag.classList.add(window.localStorage.layout)
	}
	

  // find all the svg elements under the div with class screen-layout and add the Click Event Listener to them
  // PS: do not add the EventListener to the a tag, since it causes the div to get the class of 'active'
  document.querySelectorAll('.screen-layout svg').forEach(node => {
  	// so when the svg element is clicked
  	// 1. get all the a tags under screen-layout
  	// 2. if the a tag contains the 'active' class, remove it
  	// 3. set the class of the event target (svg element) parentnode (a tag) to 'active' if it does not already have it 
  	//														(i.e. when selecting the same layout)
  	node.addEventListener('click', function(e) {
      document.querySelectorAll('.screen-layout a').forEach(anchor => {
        if (anchor.classList.contains('active')){
          anchor.classList.remove('active')
        }
      });
  		if (!e.target.parentNode.classList.contains('active')){
  			e.target.parentNode.classList.add('active'); 			
  		}
  		var sbStatusClasses = ['default', 'hide-left', 'hide-right', 'hide-both'];
  		var mainTag = document.querySelector('main');
  		sbStatusClasses.forEach(function(classname) {
  			if (mainTag.classList.contains(classname)) {
  				mainTag.classList.remove(classname);
  			}
  		});
  		if (e.target.parentNode.classList.contains('sb-right')) {
				window.localStorage.setItem('trigger','sb-right');
				window.localStorage.setItem('layout','hide-left');
  			mainTag.classList.add('hide-left');
  		} else if (e.target.parentNode.classList.contains('sb-left')) {
				window.localStorage.setItem('trigger','sb-left');
				window.localStorage.setItem('layout','hide-right');
  			mainTag.classList.add('hide-right');
  		} else if (e.target.parentNode.classList.contains('no-sb')) {
				window.localStorage.setItem('trigger','no-sb');
				window.localStorage.setItem('layout','hide-both');
  			mainTag.classList.add('hide-both');
  		} else {
				window.localStorage.setItem('trigger','default');
				window.localStorage.setItem('layout','default');
  			mainTag.classList.add('default');
  		}
			e.preventDefault();
			
			if($("h3[id^='open-issues-in-'] + table").length) {
				resizeTable()
			}
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

  // Define viewportWidth variable
  var viewportWidth;

  // Set/update the viewportWidth value
  var setViewportWidth = function () {
    viewportWidth = window.innerWidth || document.documentElement.clientWidth;
  }

  // Get the clicked element in die right sidebar
  var getClickedLink = function () {
    if (viewportWidth < 576) {
      document.querySelectorAll('.book-toc nav a').forEach(anc => {
        anc.onclick = function() { 
          var sbStatusClasses = ['default', 'hide-left', 'hide-right', 'hide-both'];
          var mainTag = document.querySelector('main');
          sbStatusClasses.forEach(function(classname) {
            if (mainTag.classList.contains(classname)) {
              mainTag.classList.remove(classname);
            }
          });
          mainTag.classList.add('default');

          var elem = document.getElementById(anc.hash.replace('#',''));
          elem.scrollIntoView();

        };
      });      
    } else {
      document.querySelectorAll('.book-toc nav a').forEach(anc => {
        anc.onclick = function(e) { 
					var elem = document.getElementById(anc.hash.replace('#',''));
					var url = window.location.protocol + "//" + window.location.host + window.location.pathname + anc.getAttribute("href");    
					window.history.pushState({ path: url }, '', url);
					$('html,body').animate({scrollTop: elem.offsetTop + 240},100)
					e.preventDefault()
        };
      });
    };
  };

  // Set our initial width and log it
  setViewportWidth();
  getClickedLink();

  // On resize events, recalculate and log
  window.addEventListener('resize', function () {
    setViewportWidth();
    getClickedLink();
	}, false);

	function resizeTable() {
		var containerWidth = $('.markdown').width();
		var table = $("h3[id^='open-issues-in-'] + table");
		$("h3[id^='open-issues-in-'] + table").width(containerWidth)
	
		$("h3[id^='open-issues-in-'] + table tbody>tr").each(function () {
			$(this).find('td').eq(0).css({maxWidth: containerWidth * 0.12 + 'px'})
			$(this).find('td').eq(1).css({maxWidth: containerWidth * 0.6 + 'px'})
			$(this).find('td').eq(2).css({maxWidth: containerWidth * 0.24 + 'px'})
			$(this).find('td').eq(3).css({maxWidth: containerWidth * 0.12 + 'px'})
		})
	}
	if($("h3[id^='open-issues-in-'] + table").length) {
		resizeTable()
	}

	$(window).resize(function () {
		if($("h3[id^='open-issues-in-'] + table").length) {
			resizeTable()
		}
	}) 
});

function checkHash() {
	if($('.docs').length) {
		if(window.location.hash) {

			var elem = document.getElementById(window.location.hash.replace('#',''));
			$('html,body').animate({scrollTop: elem.offsetTop + 240},100)
		}
	}
}

function isScrollToFinished() {
	const checkIfScrollToIsFinished = setInterval(() => {
			if ($(window).scrollTop() === 0) {
					clearInterval(checkIfScrollToIsFinished);
					checkHash();
			}
	}, 25);
}

window.addEventListener('DOMContentLoaded', (event) => {
	isScrollToFinished();
	setTimeout(function() {
    window.scrollTo(0, 0);
  }, 1);
});