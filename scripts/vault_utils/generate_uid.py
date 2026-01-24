import re

def extract_consonants(word):
    word = re.sub(r"[aeiouyAEIOUY]", "", word)
    return "".join([c.upper() for c in word if c.isalpha()])

def generate_uid(title, version="00-00"):
    words = title.strip().split()
    if len(words) < 2:
        words.append(words[0])
    first, second = words[0], words[1]
    fc = extract_consonants(first)[:2] or first[0]*2
    sc = extract_consonants(second)[:2] or second[0]*2
    uid = f"{fc}-{sc}_{version}"
    return uid

if __name__ == "__main__":
    title = input("Enter a title or phrase: ")
    uid = generate_uid(title)
    print("Generated UID:", uid)
