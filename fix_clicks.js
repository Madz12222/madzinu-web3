// Force all buttons and interactive elements to be clickable
const style = document.createElement('style');
style.innerHTML = `
  button, input, a, .clickable, [onclick] {
    pointer-events: auto !important;
    cursor: pointer !important;
    position: relative;
    z-index: 999999;
  }
  .modal, .overlay, .backdrop {
    pointer-events: auto;
  }
`;
document.head.appendChild(style);
