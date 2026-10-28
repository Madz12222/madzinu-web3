with open("server.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace require statements with imports
content = content.replace("const express = require('express');", "import express from 'express';")
content = content.replace("const cors = require('cors');", "import cors from 'cors';")
content = content.replace("const bodyParser = require('body-parser');", "import bodyParser from 'body-parser';")

with open("server.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Converted server.js to ES module imports!")
