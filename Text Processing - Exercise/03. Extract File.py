path = input()
extension = ""
name = ""
is_extension = False
for ch in reversed(path):
    if ch != "." and not is_extension:
        extension += ch
    else:
        is_extension = True
    if ch != "\\" and is_extension and ch != ".":
        name += ch
    elif ch == "\\":
        break
print(f"File name: {name[::-1]}")
print(f"File extension: {extension[::-1]}")

