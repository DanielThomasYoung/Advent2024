def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total = 0
    left = {}
    right = {}

    for line in lines:
        numbers = line.split()
        increment_dict(left, int(numbers[0]))
        increment_dict(right, int(numbers[1]))

    for key, value in left.items():
        if key in right:
            total += key * value * right[key]

    print(total)


def increment_dict(dictionary, value):
    if value in dictionary:
        dictionary[value] += 1
    else:
        dictionary[value] = 1


if __name__ == "__main__":
    main()
