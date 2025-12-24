with open("input.txt", "r") as file:
    input_data = file.read()

lines = input_data.splitlines()

max_len = max(len(line) for line in lines)
grand_total = 0

nums = []
op = '+' 

for i in range(max_len - 1, -1, -1):
    col = "".join(line[i] if i < len(line) else " " for line in lines)

    if not col.strip():
        if nums:
            res = nums[0]
            for n in nums[1:]:
                res = (res * n) if op == '*' else (res + n)
            grand_total += res
            nums = [] 
            op = '+'
        continue

    digit = "".join(c for c in col if c.isdigit())
    if digit:
        nums.append(int(digit))
    
    if '*' in col: op = '*'
    elif '+' in col: op = '+'

if nums:
    res = nums[0]
    for n in nums[1:]:
        res = (res * n) if op == '*' else (res + n)
    grand_total += res

print(f"Total: {grand_total}")