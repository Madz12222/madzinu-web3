with open("server.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Fix any malformed mongoose or backslash lines
    if "mongoose" in line and "\\" in line:
        line = "import mongoose from 'mongoose';\n"
    elif "require(" in line:
        import re
        m = re.search(r'const\s+(\w+)\s*=\s*require\([\'"]([^\'"]+)[\'"]\);?', line)
        if m:
            var_name, pkg = m.groups()
            line = f"import {var_name} from '{pkg}';\n"
    new_lines.append(line)

with open("server.js", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("✅ Cleaned server.js syntax successfully!")
