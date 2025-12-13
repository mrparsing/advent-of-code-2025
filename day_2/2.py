ids = []

with open("input.txt", "r") as file:
    for line in file:
        ids.extend(line.strip().split(","))

total = 0

for interval in ids:
    start, end = interval.split("-")

    for x in range(int(start), int(end) + 1):
        s = str(x)
        n = len(s)

        divisors = [d for d in range(1, n) if n % d == 0]

        for d in divisors:
            parts = [s[i:i+d] for i in range(0, n, d)]

            if all(p == parts[0] for p in parts):
                total += x
                break

print(total)