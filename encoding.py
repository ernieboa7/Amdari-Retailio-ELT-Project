import chardet

# 1. Detect encoding
with open("data/sales.csv", "rb") as f:
    raw = f.read()
result = chardet.detect(raw)
print(result)  

# 2. Convert to UTF-8
encoding = result["encoding"] or "latin1"
text = raw.decode(encoding, errors="replace")

with open("data/sales.csv", "w", encoding="utf-8", newline="") as f:
    f.write(text)
