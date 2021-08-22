def check (half_ticket):
    max_count_1 = 0
    max_count_2 = 0
    max_count_3 = 0
    max_count_4 = 0

    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    previous = half_ticket[0]
    for i in half_ticket:
        if i == "@" and (i == previous or count_1 == 0):
            count_1 += 1
        else:
            if max_count_1 < count_1:
                max_count_1 = count_1
            count_1 = 0
        if i == "#" and (i == previous or count_2 == 0):
            count_2 += 1
        else:
            if max_count_2 < count_2:
                max_count_2 = count_2
            count_2 = 0
        if i == "$" and (i == previous or count_3 == 0):
            count_3 += 1
        else:
            if max_count_3 < count_3:
                max_count_3 = count_3
            count_3 = 0
        if i == "^" and (i == previous or count_4 == 0):
            count_4 += 1
        else:
            if max_count_4 < count_4:
                max_count_4 = count_4
            count_4 = 0
        previous = i
    max_count_1 = max(max_count_1, count_1)
    max_count_2 = max(max_count_2, count_2)
    max_count_3 = max(max_count_3, count_3)
    max_count_4 = max(max_count_4, count_4)

    max_count = max(max_count_1, max_count_2, max_count_3, max_count_4)
    if max_count >= 6:
        if max_count == max_count_1:
            return [max_count_1, "@"]
        elif max_count == max_count_2:
            return [max_count_2, "#"]
        elif max_count == max_count_3:
            return [max_count_3, "$"]
        elif max_count == max_count_4:
            return [max_count_4, "^"]
    else:
        return [0, 0]


tickets = input().split(", ")

for ticket in tickets:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
    else:
        first_half = ticket[:10]
        second_half = ticket[10:]

        if check(first_half)[0] >= 6 and check(second_half)[0] >= 6 and check(first_half)[1] == check(second_half)[1]:
            match_length = min(check(first_half)[0], check(second_half)[0])
            match_symbol = check(first_half)[1]
            if match_length == 10:
                print(f'ticket "{ticket}" - {match_length}{match_symbol} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {match_length}{match_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')




