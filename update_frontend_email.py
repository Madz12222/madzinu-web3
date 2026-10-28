import os

# Create or patch frontend profile handler to capture email
print("Updating frontend form modal to include Email Input Field...")

# Script to ensure email is sent in request body to backend
js_patch = """
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
"""

with open("public/email_helper.js", "w", encoding="utf-8") as f:
    f.write(js_patch)

print("Email helper script created successfully!")
