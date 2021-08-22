text = input().split()
first = text[0]
second = text[1]
total = 0
i = 0
while i < min(len(first), len(second)):
    total += ord(first[i]) * ord(second[i])
    i += 1

if len(first) > len(second):
    while i < len(first):
        total += ord(first[i])
        i += 1
elif len(second) > len(first):
    while i < len(second):
        total += ord(second[i])
        i += 1

print(total)