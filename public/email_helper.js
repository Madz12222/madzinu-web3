
// Function to capture user details including Email
function getUserAuthPayload() {
    const mobile = document.getElementById('userMobile')?.value || localStorage.getItem('user_mobile');
    const email = document.getElementById('userEmail')?.value || localStorage.getItem('user_email');
    const name = document.getElementById('userName')?.value || localStorage.getItem('user_name');
    
    // Save locally for quick access
    if (email) localStorage.setItem('user_email', email);
    if (name) localStorage.setItem('user_name', name);
    
    return { mobile, email, name };
}
