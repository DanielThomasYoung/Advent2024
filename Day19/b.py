import functools

linens = []


def main() -> int:
    global linens
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    first_line = file_lines[0].strip()
    linens = first_line.split(", ")
    total = 0

    for line in file_lines[1:]:
        total += recursion(line)

    print(total)


@functools.cache
def recursion(line: str):
    line = line.strip()
    if not line:
        return 1
    total = 0
    for linen in linens:
        if linen == line[0 : len(linen)]:
            total += recursion(line[len(linen) :])

    return total


if __name__ == "__main__":
    main()
