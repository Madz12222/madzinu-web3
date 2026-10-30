document.addEventListener('DOMContentLoaded', () => {
  const loginBtn = document.querySelector('button[onclick*="requestFast2SMSOTP"]') || document.getElementById('login-btn');
  if (loginBtn) {
    loginBtn.style.pointerEvents = 'auto';
    loginBtn.style.zIndex = '999999';
    loginBtn.onclick = function() {
      if (typeof requestFast2SMSOTP === 'function') {
        requestFast2SMSOTP();
      } else {
        console.log("Triggering login flow...");
      }
    };
  }
});
