def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    grand_total = 0

    padded_line = ["." * (len(lines[0]) + 2)]
    for line in lines:
        padded_line.append("." + line.strip() + ".")
    padded_line.append("." * (len(lines[0]) + 2))
    lines = padded_line

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "0":
                grand_total += begin_search(lines, line_index, char_index)

    print(grand_total)


def begin_search(lines, line_index, char_index):
    total = 0
    next_number = "1"
    positions = [[line_index, char_index]]
    nine_locations = []
    while positions:
        new_positions = []

        for position in positions:
            for line_offset, char_offset in [
                (position[0] - 1, position[1]),
                (position[0] + 1, position[1]),
                (position[0], position[1] - 1),
                (position[0], position[1] + 1),
            ]:
                if lines[line_offset][char_offset] == next_number:
                    if next_number == "9":
                        nine_locations.append([line_offset, char_offset])
                        total += 1
                    new_positions.append([line_offset, char_offset])

        positions = new_positions
        next_number = str(int(next_number) + 1)

    return total


if __name__ == "__main__":
    main()
