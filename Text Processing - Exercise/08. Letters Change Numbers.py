text = input().split()
total = 0
sum_total = 0

for word in text:
    number = int(word[1:-1])
    if word[0].isupper():
        total = number / (ord(word[0]) - 64)
    else:
        total = number * (ord(word[0]) - 96)
    if word[-1].isupper():
        total -= (ord(word[-1]) - 64)
    else:
        total += (ord(word[-1]) - 96)
    sum_total += total

print(f"{sum_total:.2f}")



