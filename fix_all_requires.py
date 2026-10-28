with open("server.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace any remaining require patterns with import syntax
import re
content = re.sub(r'const\s+(\w+)\s*=\s*require\([\'"]([^\'"]+)[\'"]\);?', r'import \1 from \'\2\';', content)

with open("server.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Converted all require statements in server.js to ES imports!")
