text = input()
new_text = ""
i = 0
while i < len(text):

    if text[i] == text[i-1] and i != 0:
        i += 1
        continue
    else:
        new_text += text[i]
    i += 1

print(new_text)