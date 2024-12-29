def main() -> int:
    with open("sample.txt", "r") as file:
        file_lines = file.readlines()

    total = 0

    for line in file_lines:
        num = int(line)

        for _ in range(2000):
            num = num ^ (num * 64)
            num %= 16777216
            num = num ^ (num // 32)
            num %= 16777216
            num = num ^ (num * 2048)
            num %= 16777216

        total += num

    print(total)


if __name__ == "__main__":
    main()
