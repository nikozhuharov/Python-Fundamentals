command = input()
courses = {}
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = {"count": 0, "names": []}
    courses[course_name]["names"].append(student_name)
    courses[course_name]["count"] += 1
    command = input()
courses = dict(sorted(courses.items(), key=lambda x: x[1]["count"], reverse=True))

for key, value in courses.items():
    print(f"{key}: {value['count']}")
    names_list = []
    for name in value['names']:
        names_list.append(name)
    names_list.sort()
    for name in names_list:
        print(f"-- {name}")

