offer_list = input().split(", ")
beggars = int(input())
beggars_list = []
counter = 0
for i in range(beggars):
    j = counter
    sum_offer = 0
    while j < len(offer_list):
        sum_offer += int(offer_list[j])
        j += beggars
    beggars_list.append(sum_offer)
    counter += 1
print(beggars_list)
