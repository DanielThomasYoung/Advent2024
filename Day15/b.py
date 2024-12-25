def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    moves = file_lines[0]
    robot_x = 0
    robot_y = 0

    lines = []
    for line in file_lines[1:]:
        new_line = []
        for char in line:
            if char == "#":
                new_line += ["#", "#"]
            elif char == "O":
                new_line += ["[", "]"]
            elif char == ".":
                new_line += [".", "."]
            elif char == "@":
                new_line += ["@", "."]
        lines.append(new_line)

    for line_index in range(len(lines)):
        for char_index in range(len(lines[line_index])):
            if lines[line_index][char_index] == "@":
                robot_x = char_index
                robot_y = line_index
                break

    for move in moves:
        if move == "<":
            if lines[robot_y][robot_x - 1] == "#":
                continue
            elif check_left(lines, robot_x - 1, robot_y):
                lines[robot_y][robot_x] = "."
                lines[robot_y][robot_x - 1] = "@"
                robot_x -= 1

        elif move == ">":
            if lines[robot_y][robot_x + 1] == "#":
                continue
            elif check_right(lines, robot_x + 1, robot_y):
                lines[robot_y][robot_x] = "."
                lines[robot_y][robot_x + 1] = "@"
                robot_x += 1

        elif move == "^":
            if lines[robot_y - 1][robot_x] == "#":
                continue
            elif check_up(lines, [robot_x], robot_y - 1):
                lines[robot_y][robot_x] = "."
                lines[robot_y - 1][robot_x] = "@"
                robot_y -= 1

        elif move == "v":
            if lines[robot_y + 1][robot_x] == "#":
                continue
            elif check_down(lines, [robot_x], robot_y + 1):
                lines[robot_y][robot_x] = "."
                lines[robot_y + 1][robot_x] = "@"
                robot_y += 1

        # print(move)
        # for line in lines:
        #     print(''.join(line))

    for line in lines:
        print("".join(line))

    total = 0
    for line_index in range(len(lines)):
        for char_index in range(len(lines[line_index])):
            if lines[line_index][char_index] == "[":
                total += 100 * line_index + char_index

    print(total)


def check_left(lines, x, y):
    if lines[y][x] == "#":
        return 0
    if lines[y][x] == ".":
        return 1
    if lines[y][x] == "]":
        if check_left(lines, x - 2, y):
            lines[y][x] = "."
            lines[y][x - 1] = "]"
            lines[y][x - 2] = "["
            return 1
        return 0


def check_right(lines, x, y):
    if lines[y][x] == "#":
        return 0
    if lines[y][x] == ".":
        return 1
    if lines[y][x] == "[":
        if check_right(lines, x + 2, y):
            lines[y][x] = "."
            lines[y][x + 1] = "["
            lines[y][x + 2] = "]"
            return 1
        return 0


def check_up(lines, all_x, y):
    next_x = []
    for x in all_x:
        if lines[y][x] == "#":
            return 0
        if lines[y][x] == "]":
            next_x.extend([x - 1, x])
        if lines[y][x] == "[":
            next_x.extend([x, x + 1])

    if not next_x:
        return 1
    if check_up(lines, next_x, y - 1):
        for index, x in enumerate(next_x):
            lines[y][x] = "."
            lines[y - 1][x] = "]" if index % 2 else "["
        return 1
    return 0


def check_down(lines, all_x, y):
    next_x = []
    for x in all_x:
        if lines[y][x] == "#":
            return 0
        if lines[y][x] == "]":
            next_x.extend([x - 1, x])
        if lines[y][x] == "[":
            next_x.extend([x, x + 1])

    if not next_x:
        return 1
    if check_down(lines, next_x, y + 1):
        for index, x in enumerate(next_x):
            lines[y][x] = "."
            lines[y + 1][x] = "]" if index % 2 else "["
        return 1
    return 0


if __name__ == "__main__":
    main()
