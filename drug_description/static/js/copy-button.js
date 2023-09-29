alert("Hello from your JavaScript file!");

// Define the copyToClipboard function
// function copyToClipboard(text) {
//     navigator.clipboard.writeText(text).then(function () {
//       console.log('Text successfully copied to clipboard');
//     }).catch(function (err) {
//       console.error('Unable to copy text to clipboard: ', err);
//     });
//   }
  
//   // Attach a click event listener to the copy button
//   document.addEventListener('DOMContentLoaded', function () {
//     var copyButton = document.getElementById('copy-button');
//     var resultContent = document.querySelector('.result-content');
  
//     copyButton.addEventListener('click', function () {
//       var contentText = resultContent.textContent;
//       copyToClipboard(contentText);
//     });
//   });