with open("routes/jobworkRoutes.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the require for Schema with import
old_line = "const { User, JobworkLedger, Payout } = require('../models/Schema');"
new_line = "import { User, JobworkLedger, Payout } from '../models/Schema.js';"

if old_line in content:
    content = content.replace(old_line, new_line)
else:
    # Generic fallback if spacing varies
    import re
    content = re.sub(r'const\s+\{([^}]+)\}\s*=\s*require\([\'"]([^\'"]+)[\'"]\);?', r'import {\1} from \'\2.js\';', content)

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Converted Schema require to ES import in jobworkRoutes.js!")
