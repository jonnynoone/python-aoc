with open("input.txt", "r") as f:
    directions = f.read()

floor = 0
for x in range(0, len(directions)):
    if directions[x] == "(":
        floor += 1
    elif directions[x] == ")":
        floor -= 1

print(f"The directions take Santa to floor {floor}.")