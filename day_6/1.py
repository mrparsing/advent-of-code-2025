import math

n = {}
with open("input.txt", "r") as file:
    for row in file:
        numbers = row.strip().split()
        for i in range(len(numbers)):
            if i in n:
                n[i].append(numbers[i])
            else:
                n[i] = [numbers[i]]

_sum = 0

for v in n.values():
    op = v[-1]
    if op == "*":
        _sum += math.prod(int(x) for x in v[:-1])
    elif op == "+":
        _sum += sum(int(x) for x in v[:-1])
print(_sum)