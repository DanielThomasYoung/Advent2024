def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total = 0

    for line in lines:
        chars = line.strip().split()
        target = int(chars[0][:-1])
        operands = chars[1:]
        operator_count = 2 ** (len(chars) - 2)

        for i in range(operator_count):
            partial_result = int(operands[0])
            for j in range(1, len(operands)):
                if (i // 2 ** (j - 1)) % 2 == 0:
                    partial_result += int(operands[j])
                else:
                    partial_result *= int(operands[j])
            if partial_result == target:
                total += partial_result
                break

    print(total)


if __name__ == "__main__":
    main()
