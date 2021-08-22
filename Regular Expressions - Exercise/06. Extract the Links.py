import re
pattern = r"www.[A-Za-z0-9]+(-[A-Za-z0-9]+)*(\.[a-z]+)+"
text = input()
while text:
    sites = re.finditer(pattern, text)
    for site in sites:
        print(site.group())
    text = input()