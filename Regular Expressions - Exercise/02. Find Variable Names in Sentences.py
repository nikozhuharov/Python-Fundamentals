import re
pattern = r"\b_[A-Za-z0-9]+\b"
valid_names=[]
text = input()
names = re.findall(pattern, text)

for name in names:
    valid_names.append(name[1:])
print(",".join(valid_names))