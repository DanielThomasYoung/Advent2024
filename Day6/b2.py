from time import sleep


def main() -> int:
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    total = 0
    start = [0, 0]
    line_array = []

    for line_index in range(len(lines)):
        line_array.append(list(lines[line_index].strip()))
        for char_index in range(len(lines[line_index])):
            if lines[line_index][char_index] == "^":
                start = [line_index, char_index]

    for line_index in range(len(line_array)):
        for char_index in range(len(line_array[line_index])):
            if line_array[line_index][char_index] not in ["^", "#"]:
                print("trying", line_index, char_index)
                total += try_with_obstacle(line_index, char_index, line_array, start)
                print(total)

    print(total)


def try_with_obstacle(line_index, char_index, line_array, start):
    lines_copy = line_array.copy()
    lines_copy[line_index][char_index] = "#"
    guard = start.copy()
    guard_history = set()
    direction = [-1, 0]

    while True:
        sleep(0.01)
        if (
            (guard[0] + direction[0]) < 0
            or (guard[0] + direction[0]) >= len(lines_copy)
            or (guard[1] + direction[1]) < 0
            or (guard[1] + direction[1]) >= len(lines_copy[0])
        ):
            return 0

        next_step = [guard[0] + direction[0], guard[1] + direction[1]]
        print(next_step)

        if lines_copy[next_step[0]][next_step[1]] == "#":
            direction = rotate_right(direction)
        else:
            history_key = str(guard + direction)
            print(guard_history)
            if history_key in guard_history:
                return 1
            guard_history.add(history_key)
            guard = next_step


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
