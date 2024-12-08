def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    antenae = {}
    antinodes = []

    for line_index in range(len(lines)):
        for char_index in range(len(lines[0])):
            char = lines[line_index][char_index]
            if char != "." and char != "\n":
                if char not in antenae:
                    antenae[char] = [[line_index, char_index]]
                else:
                    antenae[char].append([line_index, char_index])
                antinodes.append([line_index, char_index])

    for antena in antenae.values():
        for start_index in range(len(antena)):
            for end_index in range(start_index + 1, len(antena)):
                for i in range(max(len(lines), len(lines[0]))):
                    first_potential_antinode = [
                        (2 + i) * antena[start_index][0]
                        - (1 + i) * antena[end_index][0],
                        (2 + i) * antena[start_index][1]
                        - (1 + i) * antena[end_index][1],
                    ]
                    second_potential_antinode = [
                        (2 + i) * antena[end_index][0]
                        - (1 + i) * antena[start_index][0],
                        (2 + i) * antena[end_index][1]
                        - (1 + i) * antena[start_index][1],
                    ]

                    if (
                        first_potential_antinode not in antinodes
                        and first_potential_antinode[0] >= 0
                        and first_potential_antinode[1] >= 0
                        and first_potential_antinode[0] < len(lines)
                        and first_potential_antinode[1] < len(lines[0]) - 1
                    ):
                        antinodes.append(first_potential_antinode)
                    if (
                        second_potential_antinode not in antinodes
                        and second_potential_antinode[0] >= 0
                        and second_potential_antinode[1] >= 0
                        and second_potential_antinode[0] < len(lines)
                        and second_potential_antinode[1] < len(lines[0]) - 1
                    ):
                        antinodes.append(second_potential_antinode)

    print(len(antinodes))


if __name__ == "__main__":
    main()
