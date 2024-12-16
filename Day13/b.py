import re

import sympy as sp


def main() -> int:
    with open("input.txt", "r") as file:
        all_lines = file.readlines()

    line_groups = []
    current_group = []

    for line in all_lines:
        line = line.strip()
        if line:
            current_group.append(line)
        else:
            if current_group:
                line_groups.append(current_group)
                current_group = []
    line_groups.append(current_group)

    total = 0

    for line in line_groups:
        A = tuple(map(int, re.findall(r"\+(\d+)", line[0])))
        B = tuple(map(int, re.findall(r"\+(\d+)", line[1])))
        Prize = tuple(
            map(lambda x: int(x) + 10000000000000, re.findall(r"\=(\d+)", line[2]))
        )

        matrix = sp.Matrix([[A[0], B[0], Prize[0]], [A[1], B[1], Prize[1]]])
        matrix = matrix.rref()[0]

        if matrix[2] % 1 == 0 and matrix[5] % 1 == 0:
            total += 3 * matrix[2] + matrix[5]

    print(total)


if __name__ == "__main__":
    main()
