import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Upgraded AI response function with Platform Knowledge Base
smart_ai_js = """
    function sendMadzinuAIMessage() {
        let input = document.getElementById('ai-user-input');
        let chatBody = document.getElementById('ai-chat-messages');
        let query = input.value.trim();
        if(!query) return;

        chatBody.innerHTML += `<div style="background: #111827; padding: 8px; border-radius: 6px; color: #fff; text-align: right;"><b>You:</b> ${query}</div>`;
        input.value = "";

        let q = query.toLowerCase();
        let reply = "";

        // Smart Knowledge Base Pattern Matcher
        if (q.includes("offer") || q.includes("package") || q.includes("plan") || q.includes("server") || q.includes("price") || q.includes("cost")) {
            reply = "🚀 <b>Server Node License Tiers (14-Day Cycle):</b><br>• <b>₹2,000 Server:</b> ₹155.50/day (Total ₹2,177)<br>• <b>₹5,000 Server:</b> ₹394.64/day (Total ₹5,525)<br>• <b>₹10,000 Server:</b> ₹792.86/day (Total ₹11,100)<br>• <b>₹25,000 Server:</b> ₹1,991.07/day (Total ₹27,875)<br>• <b>₹50,000 Server:</b> ₹4,000/day (Total ₹56,000)<br>• <b>₹1,00,000 Server:</b> ₹8,000/day (Total ₹1,12,000)";
        } else if (q.includes("free") || q.includes("task") || q.includes("micro")) {
            reply = "📊 <b>Free Tier & Jobworks:</b> Complete 500 daily micro-tasks (Amazon, Flipkart, Meesho catalog pricing & SKU audits) at ₹0.20/task to earn <b>₹100 daily</b> with a ₹100 minimum withdrawal limit!";
        } else if (q.includes("referral") || q.includes("bonus") || q.includes("invite") || q.includes("share")) {
            reply = "🎁 <b>Referral Bonus:</b> Earn <b>10% - 12% dynamic referral bonuses</b> on every server node activated by your team! Enterprise servers (₹25,000+) also unlock 24K Gold Vault conversion benefits.";
        } else if (q.includes("pay") || q.includes("gpay") || q.includes("slice") || q.includes("upi") || q.includes("deposit")) {
            reply = "💳 <b>Payment Methods:</b> You can pay directly via GPay UPI (<code>madhan958@slc</code>) or Slice Bank Transfer (Account: <code>033311501076921</code>, IFSC: <code>NESF0000333</code>). Upload your UTR after payment to activate.";
        } else if (q.includes("gold") || q.includes("silver") || q.includes("vault") || q.includes("rate")) {
            reply = "👑 <b>24K Gold & Silver Vault:</b> Your INR balance is dynamically converted to live spot market gold/silver weight. Enterprise tiers (₹25k+) can redeem vouchers at Tanishq, GRT, Kalyan, and Malabar Jewellers.";
        } else if (q.includes("withdraw") || q.includes("payout") || q.includes("time")) {
            reply = "⚡ <b>Payouts:</b> Daily remunerations are logged automatically. Payout requests are verified and approved by the Master Admin terminal daily via Fast2SMS OTP security.";
        } else if (q.includes("meity") || q.includes("govt") || q.includes("company") || q.includes("madzinu") || q.includes("who")) {
            reply = "🏛️ <b>About Us:</b> Madzinu Web3 Technologies is a Govt. of India Recognized Startup entity under MeitY providing high-throughput sovereign cloud compute and autonomous jobworks.";
        } else if (q.includes("hi") || q.includes("hello") || q.includes("hey")) {
            reply = "Hello! 👋 Welcome to Madzinu Web3 Technologies AI Node. Ask me about our <b>Server Tiers, Free Micro-Tasks, Daily Earnings, Payment Methods, or Gold Vault!</b>";
        } else {
            reply = "🤖 <b>Madzinu AI Assistant:</b> Madzinu Web3 Technologies offers server nodes from ₹2,000 to ₹1,00,000 with 14-day daily returns, free 500 task jobworks (₹100/day), 10-12% referral bonuses, and 24K gold conversion. How can I assist you further with node activation?";
        }

        setTimeout(() => {
            chatBody.innerHTML += `<div style="background: #1e1b4b; padding: 8px; border-radius: 6px; color: #38bdf8; line-height: 1.4;"><b>Madzinu AI:</b> ${reply}</div>`;
            chatBody.scrollTop = chatBody.scrollHeight;
        }, 400);
    }
"""

# Replace old sendMadzinuAIMessage function
old_pattern = r'function sendMadzinuAIMessage\(\)\s*\{[\s\S]*?\}\s*\}'
if re.search(old_pattern, content):
    new_content = re.sub(old_pattern, smart_ai_js.strip(), content)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully upgraded Madzinu AI Brain in index.html!")
else:
    print("Could not locate old function, checking simple string replace...")
    # Alternative direct replacement
    idx = content.find("function sendMadzinuAIMessage()")
    if idx != -1:
        end_idx = content.find("</script>", idx)
        content = content[:idx] + smart_ai_js.strip() + "\n" + content[end_idx:]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Direct replacement successful!")
    else:
        print("Function signature not found.")
