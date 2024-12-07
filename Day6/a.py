from time import sleep


def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    line_array = []

    guard = [0, 0]
    direction = [-1, 0]

    for line_index in range(len(lines)):
        line_array.append(list(lines[line_index].strip()))
        for char_index in range(len(lines[line_index])):
            if lines[line_index][char_index] == "^":
                guard = [line_index, char_index]
                print(guard)

    while True:
        if (
            (guard[0] + direction[0]) < 0
            or (guard[0] + direction[0]) >= len(line_array)
            or (guard[1] + direction[1]) < 0
            or (guard[1] + direction[1]) >= len(line_array[0])
        ):
            break
        if lines[guard[0] + direction[0]][guard[1] + direction[1]] == "#":
            if direction == [-1, 0]:
                direction = [0, 1]
            elif direction == [0, 1]:
                direction = [1, 0]
            elif direction == [1, 0]:
                direction = [0, -1]
            elif direction == [0, -1]:
                direction = [-1, 0]

        guard = [guard[0] + direction[0], guard[1] + direction[1]]
        line_array[int(guard[0])][int(guard[1])] = "X"

        total = 0

    for line in line_array:
        for char in line:
            if char == "X":
                total += 1

    print(total)


if __name__ == "__main__":
    main()
