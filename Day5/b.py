def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    top_section = True
    total = 0

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
            for number in numbers:
                if number in bad_numbers:
                    total += reorder(numbers, order)
                    break
                if number in order:
                    bad_numbers.update(order[number])

    print(total)


def reorder(numbers, order):
    bad_numbers = {}
    for index in range(len(numbers)):
        number = numbers[index]
        if number in bad_numbers:
            new_index = bad_numbers[number]
            numbers.pop(index)
            numbers.insert(new_index, number)
            return reorder(numbers, order)
        if number in order:
            for bad_number in order[number]:
                bad_numbers[bad_number] = index

    return int(numbers[int((len(numbers) - 1) / 2)])


if __name__ == "__main__":
    main()
