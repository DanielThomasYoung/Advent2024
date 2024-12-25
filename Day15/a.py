def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    moves = file_lines[0]
    robot_x = 0
    robot_y = 0

    lines = []
    for line in file_lines[1:]:
        lines.append(list(line.strip()))

    for line_index in range(len(lines)):
        for char_index in range(len(lines[line_index])):
            if lines[line_index][char_index] == "@":
                robot_x = char_index
                robot_y = line_index

    for move in moves:
        if move == "<":
            if lines[robot_y][robot_x - 1] == "#":
                continue
            elif lines[robot_y][robot_x - 1] == "O":
                empty_check_x = robot_x - 2
                while lines[robot_y][empty_check_x] != "#":
                    if lines[robot_y][empty_check_x] == "O":
                        empty_check_x -= 1
                    else:
                        lines[robot_y][empty_check_x] = "O"
                        lines[robot_y][robot_x - 1] = "."
                        robot_x -= 1
                        break
            else:
                robot_x -= 1

        elif move == "^":
            if lines[robot_y - 1][robot_x] == "#":
                continue
            elif lines[robot_y - 1][robot_x] == "O":
                empty_check_y = robot_y - 2
                while lines[empty_check_y][robot_x] != "#":
                    if lines[empty_check_y][robot_x] == "O":
                        empty_check_y -= 1
                    else:
                        lines[empty_check_y][robot_x] = "O"
                        lines[robot_y - 1][robot_x] = "."
                        robot_y -= 1
                        break
            else:
                robot_y -= 1

        elif move == ">":
            if lines[robot_y][robot_x + 1] == "#":
                continue
            elif lines[robot_y][robot_x + 1] == "O":
                empty_check_x = robot_x + 2
                while lines[robot_y][empty_check_x] != "#":
                    if lines[robot_y][empty_check_x] == "O":
                        empty_check_x += 1
                    else:
                        lines[robot_y][empty_check_x] = "O"
                        lines[robot_y][robot_x + 1] = "."
                        robot_x += 1
                        break
            else:
                robot_x += 1

        elif move == "v":
            if lines[robot_y + 1][robot_x] == "#":
                continue

            elif lines[robot_y + 1][robot_x] == "O":
                empty_check_y = robot_y + 2
                while lines[empty_check_y][robot_x] != "#":
                    if lines[empty_check_y][robot_x] == "O":
                        empty_check_y += 1
                    else:
                        lines[empty_check_y][robot_x] = "O"
                        lines[robot_y + 1][robot_x] = "."
                        robot_y += 1
                        break
            else:
                robot_y += 1

    for line in lines:
        print("".join(line))

    total = 0
    for line_index in range(len(lines)):
        for char_index in range(len(lines[line_index])):
            if lines[line_index][char_index] == "O":
                total += 100 * line_index + char_index

    print(total)


if __name__ == "__main__":
    main()
