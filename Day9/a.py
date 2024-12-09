def main() -> int:
    with open("input.txt", "r") as file:
        line = file.readline()

    file_blocks = []
    spaces = []
    total = 0

    for index in range(len(line)):
        if index % 2:
            spaces.append(int(line[index]))
        else:
            file_blocks.append(int(line[index]))

    position = 0
    block_beginning = 0
    block_end = len(file_blocks) - 1

    while file_blocks:
        current_block = file_blocks.pop(0)
        while current_block:
            total += position * block_beginning
            position += 1
            current_block -= 1
        block_beginning += 1

        current_space = spaces.pop(0)
        while current_space:
            if not file_blocks:
                break

            total += position * block_end

            file_blocks[-1] -= 1
            if file_blocks[-1] == 0:
                file_blocks.pop()
                block_end -= 1

            position += 1
            current_space -= 1

    print(total)


if __name__ == "__main__":
    main()
