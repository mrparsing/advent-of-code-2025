with open("input.txt", "r") as file:
    for id in file:
        id = id.split(",")

sum = 0
for i in id:
    first_id, second_id = i.split("-")
    for x in range(int(first_id), int(second_id)+1):
        number = str(x)
        len_numb = len(number)
        if len_numb % 2 == 0:
            first_part = number[0:len_numb//2]
            second_part = number[len_numb//2:len_numb]
            if first_part == second_part:
                sum += int(number)
print(sum)
