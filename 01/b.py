with open("input.txt", "r") as f:
    directions = f.read()

floor = 0
for index, char in enumerate(directions):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

    if floor < 0:
        print(index + 1)
        break