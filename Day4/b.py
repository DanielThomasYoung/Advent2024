def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total = 0

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            char = lines[row][col]
            if (
                char == "A"
                and row > 0
                and row < len(lines) - 1
                and col > 0
                and col < len(lines[row]) - 1
            ):
                top_left = lines[row - 1][col - 1]
                top_right = lines[row - 1][col + 1]
                bottom_left = lines[row + 1][col - 1]
                bottom_right = lines[row + 1][col + 1]

                if (
                    top_left == "M"
                    and top_right == "M"
                    and bottom_left == "S"
                    and bottom_right == "S"
                    or top_left == "S"
                    and top_right == "M"
                    and bottom_left == "S"
                    and bottom_right == "M"
                    or top_left == "S"
                    and top_right == "S"
                    and bottom_left == "M"
                    and bottom_right == "M"
                    or top_left == "M"
                    and top_right == "S"
                    and bottom_left == "M"
                    and bottom_right == "S"
                ):
                    total += 1

    print(total)


if __name__ == "__main__":
    main()
