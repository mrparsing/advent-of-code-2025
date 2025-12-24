with open("input.txt", "r") as file:
    rows = file.read().strip().split('\n')

active_beams = set()
start_row = 0

for r, row in enumerate(rows):
    if "S" in row:
        start_row = r
        active_beams.add(row.index("S"))
        break

splits = 0
height = len(rows)
width = len(rows[0])

for r in range(start_row + 1, height):
    next_beams = set()
    
    for c in active_beams:
        current_char = rows[r][c]
        
        if current_char == "^":
            splits += 1
            
            if c - 1 >= 0:
                next_beams.add(c - 1)
            if c + 1 < width:
                next_beams.add(c + 1)
                
        else:
            next_beams.add(c)
    
    active_beams = next_beams
    
    if not active_beams:
        break

print(f"Total splits: {splits}")