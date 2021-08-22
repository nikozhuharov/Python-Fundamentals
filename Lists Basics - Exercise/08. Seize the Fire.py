fires = input().split("#")
water = int(input())
cells = []
effort = 0

for fire in fires:
    individual_fire = fire.split(" = ")
    if (individual_fire[0] == "High" and 81 <= int(individual_fire[1]) <= 125) or (individual_fire[0] == "Medium" and 51 <= int(individual_fire[1]) <= 80) or (individual_fire[0] == "Low" and 1 <= int(individual_fire[1]) <= 50):
        if water >= int(individual_fire[1]):
            cells.append(int(individual_fire[1]))
            water -= int(individual_fire[1])
            effort += 0.25*int(individual_fire[1])

print("Cells:")
for i in cells:
    print("-", str(i))
print(f"Effort: {effort:.2f}")
print("Total Fire:", str(sum(cells)))
