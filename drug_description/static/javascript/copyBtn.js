// Define the copyToClipboard function
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(function () {
      console.log('Text successfully copied to clipboard');
  }).catch(function (err) {
      console.error('Unable to copy text to clipboard: ', err);
  });
}

// Attach a click event listener to the copy button
document.addEventListener('DOMContentLoaded', function () {
  var copyButton = document.getElementById('copy-button');
  var resultContent = document.querySelector('.result-content');

  copyButton.addEventListener('click', function (e) {
      e.preventDefault(); // Prevent the default behavior of the copy button

      var contentText = resultContent.textContent;
      copyToClipboard(contentText);

      copyButton.style.backgroundColor = '#74b65a';
      copyButton.textContent = "Copied";
      copyButton.classList.add('copied');
  });
});