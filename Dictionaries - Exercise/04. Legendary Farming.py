materials_dict = {"fragments": 0, "motes": 0, "shards": 0}
is_found = False

while True:
    materials = input().split()
    for i in range(0, len(materials), 2):
        if materials[i+1].lower() not in materials_dict:
            materials_dict[materials[i+1].lower()] = int(materials[i])
        else:
            materials_dict[materials[i+1].lower()] += int(materials[i])
        for key, value in materials_dict.items():
            if key == "shards" and value >= 250:
                materials_dict[key] -= 250
                print("Shadowmourne obtained!")
                is_found = True
                break
            elif key == "fragments" and value >= 250:
                materials_dict[key] -= 250
                print("Valanyr obtained!")
                is_found = True
                break
            elif key == "motes" and value >= 250:
                materials_dict[key] -= 250
                print("Dragonwrath obtained!")
                is_found = True
                break
        if is_found:
            break
    if is_found:
        break

key_elements = {key: value for key, value in materials_dict.items()\
                if key == "shards" or key == "fragments" or key == "motes"}
sorted_key_elements = dict(sorted(key_elements.items(),\
                                  key=lambda x: x[1], reverse=True))
for key, value in sorted_key_elements.items():
    print(f"{key}: {value}")

not_key_elements = {key: value for key, value in materials_dict.items()\
                if key != "shards" and key != "fragments" and key != "motes"}
sorted_not_key_elements = dict(sorted(not_key_elements.items(),\
                                  key=lambda x: x[0]))
for key, value in sorted_not_key_elements.items():
    print(f"{key}: {value}")
