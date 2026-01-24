
import re, json, sys, hashlib
text = sys.argv[1]
tokens = re.findall(r"[A-Za-z’']+|[0-9]+", text)
obj = {
  "text": text,
  "tokens": tokens,
  "hash": hashlib.sha1(text.encode()).hexdigest()[:10]
}
print(json.dumps(obj, indent=2))
