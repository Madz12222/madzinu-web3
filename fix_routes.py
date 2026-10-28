with open("routes/jobworkRoutes.js", "r", encoding="utf-8") as f:
    content = f.read()

# Clean up any escaped backslashes in quotes across the entire file
content = content.replace("\\'", "'").replace('\\"', '"')

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Fixed quote syntax in jobworkRoutes.js!")
