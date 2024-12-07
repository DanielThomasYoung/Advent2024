from time import sleep


def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    found_locations = set()
    guard = [0, 0]
    guard_history = []
    direction = [-1, 0]

    for line_index in range(len(lines)):
        for char_index in range(len(lines[line_index])):
            if lines[line_index][char_index] == "^":
                guard = [line_index, char_index]

    while True:
        if (
            (guard[0] + direction[0]) < 0
            or (guard[0] + direction[0]) >= len(lines)
            or (guard[1] + direction[1]) < 0
            or (guard[1] + direction[1]) >= len(lines[0])
        ):
            break
        if lines[guard[0] + direction[0]][guard[1] + direction[1]] == "#":
            direction = rotate_right(direction)
        else:
            if try_rotate(guard, guard_history, direction, lines):
                found_locations.add(
                    str([guard[0] + direction[0], guard[1] + direction[1]])
                )

        guard_history.append(str(guard + direction))
        guard = [guard[0] + direction[0], guard[1] + direction[1]]

    print(len(found_locations))


def try_rotate(guard, guard_history, direction, lines):
    temp_guard = guard.copy()
    temp_direction = direction.copy()
    temp_guard_history = []
    temp_direction = rotate_right(temp_direction)

    while True:
        if (
            (temp_guard[0] + temp_direction[0]) < 0
            or (temp_guard[0] + temp_direction[0]) >= len(lines)
            or (temp_guard[1] + temp_direction[1]) < 0
            or (temp_guard[1] + temp_direction[1]) >= len(lines[0])
        ):
            break

        if lines[temp_guard[0] + temp_direction[0]][
            temp_guard[1] + temp_direction[1]
        ] == "#" or [
            temp_guard[0] + temp_direction[0],
            temp_guard[1] + temp_direction[1],
        ] == [
            guard[0] + direction[0],
            guard[1] + direction[1],
        ]:
            temp_direction = rotate_right(temp_direction)

        else:
            temp_guard = [
                temp_guard[0] + temp_direction[0],
                temp_guard[1] + temp_direction[1],
            ]

            history_key = str(temp_guard + temp_direction)
            if history_key in temp_guard_history or history_key in guard_history:
                print("found", temp_guard, temp_direction)
                return 1

            temp_guard_history.append(history_key)

    return 0


def rotate_right(direction):
    if direction == [-1, 0]:
        return [0, 1]
    elif direction == [0, 1]:
        return [1, 0]
    elif direction == [1, 0]:
        return [0, -1]
    return [-1, 0]


if __name__ == "__main__":
    main()
