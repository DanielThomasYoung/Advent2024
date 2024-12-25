from dataclasses import dataclass
from itertools import combinations


def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    lines = []

    for line_index in range(len(file_lines)):
        lines.append(list(file_lines[line_index].strip()))
        for char_index in range(len(file_lines[0].strip())):
            if file_lines[line_index][char_index] == "S":
                position = [line_index, char_index]
            elif file_lines[line_index][char_index] == "E":
                end = [line_index, char_index]
                lines[line_index][char_index] = "."

    path = []
    distance = 0

    while True:
        path.append(Path(position[0], position[1], distance))
        if position[0] == end[0] and position[1] == end[1]:
            break

        lines[position[0]][position[1]] = "#"

        if lines[position[0] + 1][position[1]] == ".":
            position[0] += 1
        elif lines[position[0] - 1][position[1]] == ".":
            position[0] -= 1
        elif lines[position[0]][position[1] + 1] == ".":
            position[1] += 1
        elif lines[position[0]][position[1] - 1] == ".":
            position[1] -= 1
        distance += 1

    total = 0

    for first, second in combinations(path, 2):
        cheat_distance = abs(first.x - second.x) + abs(first.y - second.y)
        if (
            cheat_distance <= 20
            and abs(first.steps - second.steps) - cheat_distance >= 100
        ):
            total += 1

    print(total)


@dataclass
class Path:
    y: int
    x: int
    steps: int


if __name__ == "__main__":
    main()
