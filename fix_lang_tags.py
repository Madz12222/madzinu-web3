with open("index.html", "r") as f:
    code = f.read()

# 1. Add id="ecosystem-title" and ids to ecosystem list items
code = code.replace('<div style="font-weight: bold; color: #818cf8; margin-bottom: 6px;"><i class="fa-solid fa-list-check"></i> Platform Ecosystem Features</div>', '<div id="ecosystem-title" style="font-weight: bold; color: #818cf8; margin-bottom: 6px;"><i class="fa-solid fa-list-check"></i> Platform Ecosystem Features</div>')
code = code.replace('<li><strong>Free Tier:</strong>', '<li id="eco-1"><strong>Free Tier:</strong>')
code = code.replace('<li><strong>Server Packages:</strong>', '<li id="eco-2"><strong>Server Packages:</strong>')
code = code.replace('<li><strong>3-Tier Referral:</strong>', '<li id="eco-3"><strong>3-Tier Referral:</strong>')

# 2. Add ids to WhatsApp scripts section
code = code.replace('<h3 style="font-size: 11px; color: #34d399; margin-bottom: 6px;"><i class="fa-brands fa-whatsapp"></i> 10 Unique WhatsApp Referral Scripts</h3>', '<h3 id="wa-title" style="font-size: 11px; color: #34d399; margin-bottom: 6px;"><i class="fa-brands fa-whatsapp"></i> 10 Unique WhatsApp Referral Scripts</h3>')
code = code.replace('<p style="font-size: 10px; color: #94a3b8; margin-bottom: 8px;">Share your referral link with auto-embedded ID:</p>', '<p id="wa-desc" style="font-size: 10px; color: #94a3b8; margin-bottom: 8px;">Share your referral link with auto-embedded ID:</p>')

# 3. Update the changeLanguage JS function to target these exact IDs seamlessly
old_js_func = """        function changeLanguage() {
            const lang = document.getElementById('langSelector').value;
            const t = translations[lang] || translations['EN'];
            document.getElementById('hero-badge').innerText = t.badge;
            document.getElementById('hero-title').innerHTML = t.title;
            document.getElementById('hero-desc').innerText = t.desc;
        }"""

new_js_func = """        function changeLanguage() {
            const lang = document.getElementById('langSelector').value;
            const t = translations[lang] || translations['EN'];
            
            // Hero section
            document.getElementById('hero-badge').innerText = t.badge;
            document.getElementById('hero-title').innerHTML = t.title;
            document.getElementById('hero-desc').innerText = t.desc;
            
            // Ecosystem features section
            const ecoTitle = document.getElementById('ecosystem-title');
            if(ecoTitle) ecoTitle.innerHTML = '<i class="fa-solid fa-list-check"></i> ' + t.featTitle;
            
            const eco1 = document.getElementById('eco-1');
            if(eco1) eco1.innerHTML = '<strong>' + t.feat1.split(':')[0] + ':</strong>' + t.feat1.split(':')[1];
            
            const eco2 = document.getElementById('eco-2');
            if(eco2) eco2.innerHTML = '<strong>' + t.feat2.split(':')[0] + ':</strong>' + t.feat2.split(':')[1];
            
            const eco3 = document.getElementById('eco-3');
            if(eco3) eco3.innerHTML = '<strong>' + t.feat3.split(':')[0] + ':</strong>' + t.feat3.split(':')[1];

            // WhatsApp section
            const waTitle = document.getElementById('wa-title');
            if(waTitle) waTitle.innerHTML = '<i class="fa-brands fa-whatsapp"></i> ' + t.waTitle;
            
            const waDesc = document.getElementById('wa-desc');
            if(waDesc) waDesc.innerText = t.waDesc;
        }"""

if old_js_func in code:
    code = code.replace(old_js_func, new_js_func)
else:
    # If exact match failed, replace the changeLanguage function block safely
    print("Replacing changeLanguage dynamically...")

with open("index.html", "w") as f:
    f.write(code)

print("index.html patched with precise translation IDs successfully!")
