import re

html_file = "index.html"

try:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if Email input field is already in index.html
    if 'id="userEmail"' not in content:
        # Inject Email input field right below Mobile number field
        email_field_html = '''
        <div class="input-group mb-3">
            <span class="input-group-text"><i class="bi bi-envelope"></i></span>
            <input type="email" id="userEmail" class="form-control" placeholder="Enter Official Email Address" required>
        </div>'''
        
        # Insert after userMobile input
        if 'id="userMobile"' in content:
            content = re.sub(r'(<input[^>]*id="userMobile"[^>]*>(\s*</div>)?)', r'\1' + email_field_html, content)
            print("Successfully injected Email input field into index.html!")
        else:
            print("userMobile element not found, skipping field injection.")

    # Include email_helper.js script tag before closing </body> tag
    if 'src="public/email_helper.js"' not in content and 'src="email_helper.js"' not in content:
        content = content.replace("</body>", '<script src="public/email_helper.js"></script>\n</body>')
        print("Linked public/email_helper.js script tag in index.html!")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

except Exception as e:
    print(f"Error updating index.html: {e}")
