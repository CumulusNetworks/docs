document.addEventListener('DOMContentLoaded', function () {
  function addCopyButtons(clipboard) {
    document.querySelectorAll('pre > code').forEach(function (codeBlock) {
      var div = document.createElement('div');
      div.className = 'copy-code-img';
      div.type = 'button';
      div.innerHTML =
        '<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/29-Copy-Paste/copy-paste-1.svg" width="20" height="20">';

      div.addEventListener('click', function () {
        // Remove shell prompts BEFORE copying
        var cleanedText = codeBlock.innerText.replace(
          /cumulus@.*?:~\$ /g,
          ''
        );

        clipboard.writeText(cleanedText).then(
          function () {
            div.blur();
            $(div)
              .attr('aria-label', 'Copied to clipboard!')
              .addClass('tooltip');

            setTimeout(function () {
              $(div)
                .removeAttr('aria-label')
                .removeClass('tooltip');
            }, 2000);
          },
          function (error) {
            console.error('Copy failed:', error);

            div.blur();
            div.innerText = 'Error';

            setTimeout(function () {
              div.innerText = '';
              div.innerHTML =
                '<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/29-Copy-Paste/copy-paste-1.svg" width="20" height="20">';
            }, 2000);
          }
        );
      });

      var pre = codeBlock.parentNode;
      pre.insertAdjacentElement('afterbegin', div);
    });
  }

  if (navigator && navigator.clipboard) {
    addCopyButtons(navigator.clipboard);
  } else {
    var script = document.createElement('script');
    script.src =
      'https://cdnjs.cloudflare.com/ajax/libs/clipboard-polyfill/2.7.0/clipboard-polyfill.promise.js';
    script.integrity =
      'sha256-waClS2re9NUbXRsryKoof+F9qc1gjjIhc2eT7ZbIv94=';
    script.crossOrigin = 'anonymous';

    script.onload = function () {
      addCopyButtons(clipboard);
    };

    document.body.appendChild(script);
  }
});