cards_list = input().split()
team_A = ["1","2","3","4","5","6","7","8","9","10","11"]
team_B = ["1","2","3","4","5","6","7","8","9","10","11"]
is_terminated = False

for i in cards_list:
    individual_card = i.split("-")
    if individual_card[0] == "A" and individual_card[1] in team_A:
        team_A.remove(individual_card[1])
    if individual_card[0] == "B" and individual_card[1] in team_B:
        team_B.remove(individual_card[1])
    if len(team_A) < 7 or len(team_B) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if is_terminated:
    print("Game was terminated")