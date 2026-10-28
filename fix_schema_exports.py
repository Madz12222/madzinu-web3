with open("models/Schema.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace module.exports with individual named exports or export default
if "module.exports =" in content:
    content = content.replace("module.exports =", "export")
    # Clean up common patterns
    content = content.replace("const User =", "export const User =")
    content = content.replace("const JobworkLedger =", "export const JobworkLedger =")
    content = content.replace("const Payout =", "export const Payout =")

with open("models/Schema.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Converted Schema.js to ES module exports!")
