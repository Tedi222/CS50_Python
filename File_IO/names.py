names = []
with open("names.csv") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=False):
    print(f"Hello, {name}")

