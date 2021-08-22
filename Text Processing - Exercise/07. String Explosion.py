text = input()
i = 0
new_text = ""
strength = 0

while i < len(text):
    if strength == 0 or text[i] == ">":
        new_text += text[i]
    if strength > 0 and text[i] != ">":
        strength -= 1
    if text[i] == ">":
        strength += int(text[i+1])
    i += 1

print(new_text)


