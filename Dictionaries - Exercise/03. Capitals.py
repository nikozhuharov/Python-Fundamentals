countries = input().split(", ")
capitals = input().split(", ")
all = list(zip(countries, capitals))

countries_dict = {key: value for key, value in all}

for key, value in countries_dict.items():
    print(f"{key} -> {value}")