total = 0

with open("input.txt", "r") as file:
    for row in file:
        row = row.strip()
        n = len(row)
        max_bank_joltage = 0

        for i in range(n):
            for j in range(i + 1, n):
                num = int(row[i] + row[j])
                
                if num > max_bank_joltage:
                    max_bank_joltage = num

        total += max_bank_joltage

print(total)