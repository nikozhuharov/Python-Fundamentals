def between(ch1, ch2):
    n1 = ord(ch1)
    n2 = ord(ch2)
    for i in range(n1+1, n2):
        print(chr(i), end=" ")


ch_1 = input()
ch_2 = input()

between(ch_1, ch_2)
