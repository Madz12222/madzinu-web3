with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

ai_widget = """
<!-- MADZINU AI INTEGRATION -->
<button class="floating-ai-trigger" onclick="toggleMadzinuAIChat()" title="Chat with Madzinu AI" style="position: fixed; bottom: 20px; right: 20px; background: linear-gradient(135deg, #6366f1, #ec4899); color: #fff; border: none; width: 50px; height: 50px; border-radius: 50%; font-size: 20px; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(99, 102, 241, 0.5); z-index: 9999;">
    <i class="fa-solid fa-robot"></i>
</button>

<div id="madzinu-ai-drawer" style="display: none; position: fixed; bottom: 80px; right: 20px; width: 320px; background: #111827; border: 1px solid #6366f1; border-radius: 14px; z-index: 10000; box-shadow: 0 10px 30px rgba(0,0,0,0.7); overflow: hidden;">
    <div style="background: #1e1b4b; padding: 10px 14px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #312e81;">
        <span style="font-weight: bold; color: #38bdf8; font-size: 12px;"><i class="fa-solid fa-microchip"></i> Madzinu AI Sovereign Assistant</span>
        <button onclick="toggleMadzinuAIChat()" style="background: none; border: none; color: #94a3b8; font-size: 16px; cursor: pointer;">&times;</button>
    </div>
    <div id="ai-chat-messages" style="padding: 12px; height: 250px; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; font-size: 11px;">
        <div style="background: #1e1b4b; padding: 8px; border-radius: 6px; color: #38bdf8;">
            Greetings! I am your Madzinu AI Sovereign Node Assistant linked via Vercel. How can I help you today?
        </div>
    </div>
    <div style="padding: 10px; background: #090d16; display: flex; gap: 6px; border-top: 1px solid #1f2937;">
        <input type="text" id="ai-user-input" placeholder="Ask Madzinu AI..." style="background: #090d16; border: 1px solid #334155; padding: 6px 8px; border-radius: 6px; color: #fff; font-size: 10px; width: 100%; flex-grow: 1;">
        <button onclick="sendMadzinuAIMessage()" style="background: #10b981; color: white; border: none; padding: 6px 10px; border-radius: 6px; font-size: 10px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-paper-plane"></i></button>
    </div>
</div>

<script>
    function toggleMadzinuAIChat() {
        let drawer = document.getElementById('madzinu-ai-drawer');
        drawer.style.display = drawer.style.display === 'block' ? 'none' : 'block';
    }
    function sendMadzinuAIMessage() {
        let input = document.getElementById('ai-user-input');
        let chatBody = document.getElementById('ai-chat-messages');
        let query = input.value.trim();
        if(!query) return;
        chatBody.innerHTML += `<div style="background: #111827; padding: 8px; border-radius: 6px; color: #fff; text-align: right;"><b>You:</b> ${query}</div>`;
        input.value = "";
        setTimeout(() => {
            chatBody.innerHTML += `<div style="background: #1e1b4b; padding: 8px; border-radius: 6px; color: #38bdf8;"><b>Madzinu AI:</b> Sovereign Node processed your query: '${query}'. All systems operating efficiently.</div>`;
            chatBody.scrollTop = chatBody.scrollHeight;
        }, 500);
    }
</script>
<!-- END MADZINU AI -->
"""

if "madzinu-ai-drawer" not in content:
    content = content.replace("</body>", ai_widget + "\n</body>")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully injected Madzinu AI into index.html!")
else:
    print("Madzinu AI is already present in index.html.")
