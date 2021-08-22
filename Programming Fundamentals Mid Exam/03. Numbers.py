data = [int(x) for x in input().split()]
average = sum(data) / len(data)
greater_data = [x for x in data if x > average]
sorted_data = sorted(greater_data, reverse=True)
if len(sorted_data) > 5:
    final_data = sorted_data[:5]
    final_data_str = [str(x) for x in final_data]
    print(" ".join(final_data_str))
elif len(sorted_data) > 0:
    final_data = sorted_data[:len(sorted_data)]
    final_data_str = [str(x) for x in final_data]
    print(" ".join(final_data_str))
else:
    print("No")
