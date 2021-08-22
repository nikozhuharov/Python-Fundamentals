command = input()
participants = {}
languages = {}

while command != "exam finished":
    command_list = command.split("-")
    username = command_list[0]
    if command_list[1] == "banned":
        del participants[username]
    else:
        language = command_list[1]
        points = int(command_list[2])
        if username in participants:
            if points > participants[username]:
                participants[username] = points
        else:
            participants[username] = points
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1
    command = input()

participants = dict(sorted(participants.items(), key=lambda x: x[0]))
languages = dict(sorted(languages.items(), key=lambda x: x[0]))

participants = dict(sorted(participants.items(), key=lambda x: x[1], reverse=True))
languages = dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))

print("Results:")
for key, value in participants.items():
    print(f"{key} | {value}")

print("Submissions:")
for key, value in languages.items():
    print(f"{key} - {value}")

