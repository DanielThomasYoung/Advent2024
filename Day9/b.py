from copy import deepcopy


def main() -> int:
    with open("input.txt", "r") as file:
        line = file.readline()

    original_file_blocks = []
    original_spaces = []
    filled_spaces = []
    total = 0
    block_value = 0
    position = 0

    for index in range(len(line)):
        if index % 2:
            original_spaces.append(int(line[index]))
            filled_spaces.append([])
        else:
            original_file_blocks.append(int(line[index]))

    file_blocks = deepcopy(original_file_blocks)
    spaces = deepcopy(original_spaces)
    end_value = len(file_blocks)

    while end_value:
        end_value -= 1
        end_block = file_blocks[end_value]

        for index in range(len(spaces)):
            if spaces[index] >= end_block and index < end_value:
                spaces[index] -= end_block
                filled_spaces[index].append([end_value, end_block])
                file_blocks[end_value] = 0
                break

    original_file_blocks.pop(0)
    current_block = file_blocks.pop(0)
    while current_block:
        total += position * block_value
        position += 1
        current_block -= 1

    while file_blocks:
        filled_space = filled_spaces.pop(0)
        original_space = original_spaces.pop(0)
        future_position = position + original_space

        while filled_space:
            current_space = filled_space.pop(0)
            while current_space[1]:
                total += position * current_space[0]
                position += 1
                current_space[1] -= 1
                original_space -= 1

        position = future_position

        block_value += 1
        current_block = file_blocks.pop(0)
        original_file_block = original_file_blocks.pop(0)
        future_position = position + original_file_block

        while current_block:
            total += position * block_value
            position += 1
            current_block -= 1

        position = future_position

    print(total)


if __name__ == "__main__":
    main()
