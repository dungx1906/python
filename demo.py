list_number = [1, 3, 4, 6, 8, 23, 26]

sum = 0

for number in list_number:
    if number % 2 == 0:
        sum += number

    else:
        sum -= number

    print(sum)

