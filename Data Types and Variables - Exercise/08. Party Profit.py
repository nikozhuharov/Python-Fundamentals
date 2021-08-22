party_size = int(input())
days = int(input())
d = days
i = 0
coins = 0
while(d > 0):
    i += 1
    coins += 50
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    coins -= 2*party_size
    if i % 3 == 0:
        coins -= 3*party_size
    if i % 5 == 0:
        coins += 20*party_size
        if i % 3 == 0:
            coins -= 2 *party_size
    d -= 1

print(f"{party_size} companions received {coins//party_size} coins each.")
