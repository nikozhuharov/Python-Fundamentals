names = input().split(", ")

for name in names:
    correct = True
    if 3 <= len(name) <= 16:
        for l in name:
            if not (l.isdigit() or l.isalpha() or l == "-" or l == "_"):
                correct = False
                break
        if correct:
            print(name)







