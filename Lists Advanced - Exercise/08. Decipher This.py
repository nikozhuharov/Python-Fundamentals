def replace (word: str):
    i = 0
    digit = []
    while True:
        if word[i].isdigit():
            digit.append(word[i])
        else:
            break
        i += 1
    number = "".join(digit)
    number = int(number)
    new_word = chr(number) + word[i:]
    return new_word


def change(word: str):
    word_list = [x for x in word]
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    return "".join(word_list)


words = input().split()
new_words = []
for word in words:
    word = replace(word)
    word = change(word)
    new_words.append(word)

print(" ".join(new_words))