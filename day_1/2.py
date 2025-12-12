counter = 0
sum = 50

with open("input.txt", "r") as file:
    for row in file:
        row = row.strip()
        direction = row[0]
        value = int(row[1:])

        if direction == "L":
            for i in range(value):
                sum = (sum - 1) % 100
                if sum == 0:
                    counter += 1
        else:
            for i in range(value):
                sum = (sum + 1) % 100
                if sum == 0:
                    counter += 1

print(counter)