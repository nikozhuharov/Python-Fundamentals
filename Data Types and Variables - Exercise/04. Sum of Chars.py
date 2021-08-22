n = int(input())
sum = 0
for i in range (n):
    l = input()
    sum += ord(l)

print("The sum equals: " + str(sum))