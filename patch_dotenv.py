with open("server.js", "r", encoding="utf-8") as f:
    content = f.read()

if "require('dotenv').config()" not in content:
    content = "require('dotenv').config();\n" + content
    with open("server.js", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully added dotenv loader to server.js!")
else:
    print("dotenv already configured in server.js!")
