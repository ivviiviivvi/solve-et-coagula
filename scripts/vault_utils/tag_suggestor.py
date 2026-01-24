def suggest_tags(text):
    tags = []
    if "feedback" in text: tags.append("#feedback")
    if "uid" in text.lower(): tags.append("#uid")
    if "archive" in text: tags.append("#fossil")
    if "obsidian" in text: tags.append("#obsidian")
    if "symbol" in text: tags.append("#glyph")
    return tags

if __name__ == "__main__":
    text = input("Paste sample content: ")
    tags = suggest_tags(text)
    print("Suggested tags:", " ".join(tags))
