files = ["index.html", "public/index.html"]

for filepath in files:
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except FileNotFoundError:
        continue

    # Update body background to a rich gradient with light text
    content = content.replace(
        "background-color: var(--bg-color);",
        "background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #090d16 100%);"
    )

    with open(filepath, "w") as f:
        f.write(content)
    print(f"Updated background gradient in {filepath}")

