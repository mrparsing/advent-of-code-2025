total = 0

with open("input.txt", "r") as file:
    for row in file:
        row = row.strip()
        n = len(row)
        
        to_remove = n - 12
        stack = []

        for d in row:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)
        total += int("".join(stack[:12]))
print(total)