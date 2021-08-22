import re
pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
text = input()

names = re.findall(pattern, text)
for name in names:
    print(name, end=" ")
