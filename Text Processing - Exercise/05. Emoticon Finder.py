text = input()
i = 0
while i < len(text):
    if text[i] == ":":
        print(text[i]+text[i+1])
    i += 1

