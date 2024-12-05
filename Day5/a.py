def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total = 0
    top_section = True
    order = {}

    for line in lines:
        line = line.strip()
        if not line:
            top_section = False
            continue

        if top_section:
            numbers = line.split("|")

            if numbers[1] not in order:
                order[numbers[1]] = {numbers[0]}
            else:
                order[numbers[1]].add(numbers[0])

        else:
            numbers = line.split(",")
            bad_numbers = set()
            good_line = True
            for number in numbers:
                if number in bad_numbers:
                    good_line = False
                    break
                if number in order:
                    bad_numbers.update(order[number])

            if good_line:
                total += int(numbers[int((len(numbers) - 1) / 2)])

    print(total)


if __name__ == "__main__":
    main()
