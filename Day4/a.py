def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total = 0

    for x_row in range(len(lines)):
        for x_col in range(len(lines[x_row])):
            char = lines[x_row][x_col]
            if char == "X":
                x_rows = []
                x_cols = []

                if x_row == 0:
                    x_rows = [0, 1]
                elif x_row == len(lines) - 1:
                    x_rows = [len(lines) - 2, len(lines) - 1]
                else:
                    x_rows = [x_row - 1, x_row, x_row + 1]

                if x_col == 0:
                    x_cols = [0, 1]
                elif x_col == len(lines[x_row]) - 1:
                    x_cols = [len(lines[x_row]) - 2, len(lines[x_row]) - 1]
                else:
                    x_cols = [x_col - 1, x_col, x_col + 1]

                for m_row in x_rows:
                    for m_col in x_cols:
                        if lines[m_row][m_col] == "M":
                            direction = (m_row - x_row, m_col - x_col)

                            a_row = m_row + direction[0]
                            a_col = m_col + direction[1]
                            if (
                                a_row < 0
                                or a_row >= len(lines)
                                or a_col < 0
                                or a_col >= len(lines[x_row])
                            ):
                                continue

                            if lines[a_row][a_col] == "A":
                                s_row = a_row + direction[0]
                                s_col = a_col + direction[1]

                                if (
                                    s_row < 0
                                    or s_row >= len(lines)
                                    or s_col < 0
                                    or s_col >= len(lines[x_row])
                                ):
                                    continue

                                if lines[s_row][s_col] == "S":
                                    total += 1

    print(total)


if __name__ == "__main__":
    main()
