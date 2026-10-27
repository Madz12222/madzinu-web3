with open("index.html", "r") as f:
    content = f.read()

partners_code = """
<div style="margin-top: 15px; background: #0d1322; padding: 12px; border-radius: 10px; border: 1.5px solid #1f2937;">
    <h3 style="font-size: 11px; color: #f59e0b; margin-bottom: 8px;">💎 24K Gold & Voucher Partners</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
        <a href="https://www.tanishq.co.in" target="_blank" style="background: #0f172a; padding: 8px; border-radius: 8px; color: #fff; text-decoration: none; font-size: 10px; font-weight: bold; border: 1px solid #1e293b; display: block; text-align: center;">Tanishq</a>
        <a href="https://www.grtjewels.com" target="_blank" style="background: #0f172a; padding: 8px; border-radius: 8px; color: #fff; text-decoration: none; font-size: 10px; font-weight: bold; border: 1px solid #1e293b; display: block; text-align: center;">GRT Jewellers</a>
        <a href="https://www.swiggy.com" target="_blank" style="background: #0f172a; padding: 8px; border-radius: 8px; color: #fff; text-decoration: none; font-size: 10px; font-weight: bold; border: 1px solid #1e293b; display: block; text-align: center;">Swiggy</a>
        <a href="https://www.zomato.com" target="_blank" style="background: #0f172a; padding: 8px; border-radius: 8px; color: #fff; text-decoration: none; font-size: 10px; font-weight: bold; border: 1px solid #1e293b; display: block; text-align: center;">Zomato</a>
    </div>
</div>
"""

if "24K Gold & Voucher Partners" not in content:
    content = content.replace("</body>", partners_code + "\n</body>")
    with open("index.html", "w") as f:
        f.write(content)
    print("Partners section added successfully!")
else:
    print("Already added!")
