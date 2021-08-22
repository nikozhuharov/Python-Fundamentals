import re
n = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
for _ in range(n):
    barcode = input()
    match = re.findall(pattern, barcode)
    if match:
        digits = re.findall(r"\d", barcode)
        if digits:
            print(f'Product group: {"".join(digits)}')
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")

