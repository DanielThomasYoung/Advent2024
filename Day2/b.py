def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()
    total = 0

    for line in lines:
        numbers = line.split()

        if single_line(numbers, True):
            total += 1
        elif single_line(list(reversed(numbers)), True):
            total += 1
        elif single_line(numbers, False):
            total += 1
        elif single_line(list(reversed(numbers)), False):
            total += 1

    print(total)


def single_line(numbers, increasing):
    safe = True
    tolerated = False
    previous = int(numbers[0])

    for index in range(1, len(numbers)):
        breaking = False

        if increasing:
            if int(numbers[index]) <= previous or int(numbers[index]) > previous + 3:
                breaking = True
        elif int(numbers[index]) >= previous or int(numbers[index]) < previous - 3:
            breaking = True

        if breaking:
            if not tolerated:
                tolerated = True
            else:
                safe = False
                break
        else:
            previous = int(numbers[index])

    return safe


if __name__ == "__main__":
    main()
