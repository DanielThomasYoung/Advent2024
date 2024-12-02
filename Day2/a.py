with open("sample.txt", "r") as file:
    lines = file.readlines()

total = 0

for line in lines:
    numbers = line.split()

    safe = True
    increasing = False

    if int(numbers[1]) > int(numbers[0]):
        increasing = True
    previous = int(numbers[0])

    for index in range(1, len(numbers)):
        if increasing:
            if int(numbers[index]) <= previous or int(numbers[index]) > previous + 3:
                safe = False
                break
        elif int(numbers[index]) >= previous or int(numbers[index]) < previous - 3:
            safe = False
            break
        previous = int(numbers[index])

    if safe:
        total += 1

print(total)
