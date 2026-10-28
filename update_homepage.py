with open("server.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure path and url modules are imported for ES modules
if "import path" not in content:
    content = "import path from 'path';\nimport { fileURLToPath } from 'url';\n" + content

# 2. Define __dirname for ES module scope if not already defined
if "__dirname" not in content:
    dirname_def = "\nconst __filename = fileURLToPath(import.meta.url);\nconst __dirname = path.dirname(__filename);\n"
    content = dirname_def + content

# 3. Add the root route if it doesn't already exist
if "app.get('/')" not in content and 'app.get("/")' not in content:
    root_route = """
// Serve the main webpage at the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
"""
    if "app.listen" in content:
        content = content.replace("app.listen", root_route + "\napp.listen")
    else:
        content += "\n" + root_route

with open("server.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Successfully updated server.js with the root webpage route!")
