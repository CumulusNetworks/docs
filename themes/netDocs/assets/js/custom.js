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

});
