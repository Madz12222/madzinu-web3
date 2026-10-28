with open("routes/jobworkRoutes.js", "r", encoding="utf-8") as f:
    content = f.read()

import re
# Replace require statements with ES imports
content = re.sub(r'const\s+(\w+)\s*=\s*require\([\'"]([^\'"]+)[\'"]\);?', r'import \1 from \'\2\';', content)

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Converted all requires in jobworkRoutes.js to imports!")
