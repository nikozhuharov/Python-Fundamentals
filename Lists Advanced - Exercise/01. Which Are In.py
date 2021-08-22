collection_1 = input().split(", ")
collection_2 = input().split(", ")
new_collection = []
for word_1 in collection_1:
    for word_2 in collection_2:
        if word_1 in word_2:
            new_collection.append(word_1)
            break
print(new_collection)
