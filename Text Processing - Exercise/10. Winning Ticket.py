tickets = input().split(", ")
winning_combinations = []
for i in range(10, 5, -1):
    winning_combinations.append(i * "@")
    winning_combinations.append(i * "#")
    winning_combinations.append(i * "$")
    winning_combinations.append(i * "^")
is_win = False

for ticket in tickets:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
    else:
        first_half = ticket[:10]
        second_half = ticket[10:]
        for i in winning_combinations:
            if i in first_half and i in second_half:
                if len(i) == 10:
                    print(f'ticket "{ticket}" - {len(i)}{i[0]} Jackpot!')
                else:
                    print(f'ticket "{ticket}" - {len(i)}{i[0]}')
                is_win = True
                break
        if not is_win:
            print(f'ticket "{ticket}" - no match')




