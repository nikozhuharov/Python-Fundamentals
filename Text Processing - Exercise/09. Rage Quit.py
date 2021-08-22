text = input()
i = 0
end = -1
repeat_text = ""
while i < len(text):
    if text[i].isdigit():
        if i != len(text) - 1:
            if text[i+1].isdigit():
                number = int(text[i:i+2])
            else:
                number = int(text[i])
        else:
            number = int(text[i])
        repeat_text += number*text[end+1:i].upper()
        if number < 10:
            end = i
        else:
            end = i + 1
            i += 1
    i += 1
unique_list = []
counter = 0
for ch in repeat_text:
    if ch not in unique_list:
        unique_list.append(ch)
        counter += 1

print(f"Unique symbols used: {counter}")
print(repeat_text)



