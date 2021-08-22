quantity = int(input())
days = int(input())
i = 0
spirit = 0
budget = 0
count_days = days

while count_days > 0:
    i += 1
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += quantity * 2
        spirit += 5
    if i % 3 == 0:
        budget += quantity*8
        spirit += 13
    if i % 5 == 0:
        budget += quantity*15
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        budget += 23
    count_days -= 1

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")

