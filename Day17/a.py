from dataclasses import dataclass


def main() -> int:
    with open("input.txt", "r") as file:
        A = int(file.readline())
        B = 0
        C = 0
        program = list(map(int, file.readline().split(",")))

    pointer = 0
    output = []

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        if opcode == 0:
            A = A // (2 ** combo(A, B, C, operand))
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = combo(A, B, C, operand) % 8
        elif opcode == 3:
            if A:
                pointer = operand
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            output.append(str(combo(A, B, C, operand) % 8))
        elif opcode == 6:
            B = A // (2 ** combo(A, B, C, operand))
        elif opcode == 7:
            C = A // (2 ** combo(A, B, C, operand))

        pointer += 2

    print(",".join(output))


def combo(A, B, C, operand):
    if operand < 4:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C


if __name__ == "__main__":
    main()
