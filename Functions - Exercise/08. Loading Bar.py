def loading_bar(num):
    n = num/10
    if n == 10:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{num}% [", end="")
        for i in range(10):
            if i < n:
                print("%", end="")
            else:
                print(".", end="")
        print("]")
        print("Still loading...")


n = int(input())
loading_bar(n)