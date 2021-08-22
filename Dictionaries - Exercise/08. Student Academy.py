n = int(input())
records = {}
records_avg = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name not in records:
        records[name] = [grade]
    else:
        records[name].append(grade)

for key, value in records.items():
    average = sum(value)/len(value)
    if average >= 4.5:
        records_avg[key] = average

records_avg = dict(sorted(records_avg.items(), key=lambda x: x[1], reverse=True))

for key, value in records_avg.items():
    print(f"{key} -> {value:.2f}")
