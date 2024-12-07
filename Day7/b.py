def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total = 0

    for line in lines:
        chars = line.strip().split()
        target = int(chars[0][:-1])
        operands = chars[1:]
        operator_count = 3 ** (len(chars) - 2)

        for i in range(operator_count):
            partial_result = int(operands[0])
            for j in range(1, len(operands)):
                op = (i // 3 ** (j - 1)) % 3
                if op == 0:
                    partial_result += int(operands[j])
                elif op == 1:
                    partial_result *= int(operands[j])
                else:
                    partial_result = int(str(partial_result) + operands[j])
            if partial_result == target:
                total += partial_result
                break

    print(total)


if __name__ == "__main__":
    main()
