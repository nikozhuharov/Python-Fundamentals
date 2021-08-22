text1 = input()
text2 = input()

n = len(text1)

for i in range(n):
    if text1[i] != text2[i]:
        for j in range(i+1):
            print(text2[j], end="")
        for k in range(i+1,n):
            print(text1[k], end="")
        print()


