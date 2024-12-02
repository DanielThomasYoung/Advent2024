with open("input.txt", "r") as file:
    lines = file.readlines()

total = 0
left = []
right = []

for line in lines:
    numbers = line.split()
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))

left.sort()
right.sort()

for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)
