def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    lock_and_keys = "".join(file_lines).split("\n\n")
    locks = []
    keys = []

    for thing in lock_and_keys:
        lines = thing.split("\n")
        matrix = [list(line) for line in lines]
        transposed_matrix = list(zip(*matrix))

        tumblers = []

        for line in transposed_matrix:
            tumblers.append(line.count("#"))

        if thing[0][0] == "#":
            locks.append(tumblers)
        else:
            keys.append(tumblers)

    total = 0

    for lock in locks:
        for key in keys:
            match = True
            for i in range(5):
                if lock[i] + key[i] > 7:
                    match = False
                    break

            if match:
                total += 1

    print(total)


if __name__ == "__main__":
    main()
