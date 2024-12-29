def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    sequences = {}

    for line in file_lines:
        num = int(line)
        change = []
        added = set()

        for _ in range(2000):
            previous = num % 10
            num = num ^ (num * 64)
            num %= 16777216
            num = num ^ (num // 32)
            num %= 16777216
            num = num ^ (num * 2048)
            num %= 16777216

            final = num % 10
            change.append(final - previous)

            if len(change) > 3:
                key = str(change[-4:])
                if key not in added:
                    if key in sequences:
                        sequences[key] += final
                    else:
                        sequences[key] = final
                added.add(key)

            previous = final
    print(max(sequences.values()))


if __name__ == "__main__":
    main()
