def main() -> int:
    program = [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 1, 5, 5, 3, 0]
    # program = [0,3,5,4,3,0]
    # program = [4,1,5,5,3,0]
    current = 1
    starting_A = 1

    while True:
        A = starting_A
        B = 0
        C = 0
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
                output.append(combo(A, B, C, operand) % 8)
            elif opcode == 6:
                B = A // (2 ** combo(A, B, C, operand))
            elif opcode == 7:
                C = A // (2 ** combo(A, B, C, operand))

            pointer += 2

        print(oct(starting_A)[2:])
        print(output)

        if output == program:
            break

        if output[-current:] == program[-current:]:
            starting_A *= 8
            current += 1
        else:
            starting_A += 1
        # sleep(0.1)


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
