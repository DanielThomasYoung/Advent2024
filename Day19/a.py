from dataclasses import dataclass
from time import sleep


def main() -> int:
    with open("sample.txt", "r") as file:
        file_lines = file.readlines()

    first_line = file_lines[0].strip()
    linens = first_line.split(", ")
    total = 0

    for line in file_lines[1:]:
        if recursion(line, linens) > 0:
            total += 1

    print(total)


def recursion(line: str, linens):
    line = line.strip()
    if not line:
        return 1
    total = 0
    for linen in linens:
        if linen == line[0 : len(linen)]:
            total += recursion(line[len(linen) :], linens)

    return total


@dataclass
class Position:
    pos_x: int
    pos_y: int
    distance: int


if __name__ == "__main__":
    main()
