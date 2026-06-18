document.addEventListener('DOMContentLoaded', function () {
  function addCopyButtons(clipboard) {
    document.querySelectorAll('pre > code').forEach(function (codeBlock) {
      var div = document.createElement('div');
      div.className = 'copy-code-img';
      div.type = 'button';
      div.innerHTML = "<img src=\"https://icons.cumulusnetworks.com/01-Interface-Essential/29-Copy-Paste/copy-paste-1.svg\" width=\"20\" height=\"20\">";

      div.addEventListener('click', function (event) {
        clipboard.writeText(codeBlock.innerText).then(function () {
            div.blur();
            $(div).attr('aria-label', 'Copied to clipboard!').addClass('tooltip');
            setTimeout(function () {
                $(div).removeAttr('aria-label', 'Copied to clipboard!').removeClass('tooltip');
            }, 2000);
        }, function (error) {
            div.blur();
            div.innerText = 'Error';
            setTimeout(function () {
              div.innerText = '';
              div.innerHTML = "<img src=\"https://icons.cumulusnetworks.com/01-Interface-Essential/29-Copy-Paste/copy-paste-1.svg\" width=\"20\" height=\"20\">";
            }, 2000);
        });
    async function cleanClipboard() {
    try {
        let text = await navigator.clipboard.readText();

        // Remove specific text
        const textToRemove = "cumulus@switch:~$ ";
        text = text.replaceAll(textToRemove, "");

        await navigator.clipboard.writeText(text);
        console.log("Clipboard updated:", text);
    } catch (err) {
        console.error("Failed to access clipboard:", err);
    }
}

cleanClipboard();

    });

      var pre = codeBlock.parentNode;
      pre.insertAdjacentElement('afterbegin', div);
    });
  }

  if (navigator && navigator.clipboard) {
    addCopyButtons(navigator.clipboard);
  } else {
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/clipboard-polyfill/2.7.0/clipboard-polyfill.promise.js';
    script.integrity = 'sha256-waClS2re9NUbXRsryKoof+F9qc1gjjIhc2eT7ZbIv94=';
    script.crossOrigin = 'anonymous';
    script.onload = function() {
        addCopyButtons(clipboard);
    };
  
    document.body.appendChild(script);
  }
});

