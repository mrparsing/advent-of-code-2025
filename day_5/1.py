with open("input.txt") as file:
    blocks = file.read().strip().split("\n\n")

    ranges = blocks[0]
    id = [x for x in blocks[1].split("\n")]

ranges = ranges.split("\n")

counter = 0
for x in id:
    for r in ranges:
        a, b = r.split("-")
        if int(a) <= int(x) <= int(b):
            counter += 1
            break
print(counter)