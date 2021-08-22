notebook = {}
words = input().split(' | ')
for word in words:
    word_arg = word.split(": ")
    if word_arg[0] not in notebook:
        notebook[word_arg[0]] = [word_arg[1]]
    else:
        notebook[word_arg[0]].append(word_arg[1])

for word in notebook:
    notebook[word].sort(key=lambda x: -len(x))

new_words = input().split(" | ")
command = input()

if command == "Test":
    for new_word in new_words:
        if new_word in notebook:
            print(f"{new_word}:")
            for definition in notebook[new_word]:
                print(f" -{definition}")
elif command == "Hand Over":
    sorted_notebook = dict(sorted(notebook.items(), key=lambda x: x[0]))
    for word in sorted_notebook:
        print(word, end=" ")


