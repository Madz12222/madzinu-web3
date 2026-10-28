with open("routes/jobworkRoutes.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace module.exports with export default
content = content.replace("module.exports = router;", "export default router;")
# Ensure express is imported using ES module syntax if needed
if "const express = require('express');" in content:
    content = content.replace("const express = require('express');", "import express from 'express';")

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Updated jobworkRoutes.js to use ES module export!")
