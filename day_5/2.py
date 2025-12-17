with open("input.txt") as file:
    blocks = file.read().strip().split("\n\n")

    ranges = blocks[0]

ranges = ranges.split("\n")

intervals = []

for r in ranges:
    a, b = map(int, r.split("-"))
    intervals.append((a, b))
intervals.sort()

merged = []
start, end = intervals[0]

for a, b in intervals[1:]:
    if a <= end + 1:
        end = max(end, b)
    else:
        merged.append((start, end))
        start, end = a, b
merged.append((start, end))

count = sum(b - a + 1 for a, b in merged)
print(count)