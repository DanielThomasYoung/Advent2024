def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()
        file.seek(0)
        file_contents = file.read()

    parts = "".join(file_lines).split("\n\n")

    assignments = parts[0].strip().splitlines()
    logic = parts[1].strip().splitlines()

    states = {}
    answer_length = file_contents.count("z")

    for assignment in assignments:
        split = assignment.split(": ")
        states[split[0]] = int(split[1])

    while True:
        for line in logic:
            split = line.split(" -> ")
            inputs = split[0].split(" ")
            output = split[1]

            if inputs[0] in states and inputs[2] in states:
                if inputs[1] == "AND":
                    states[output] = states[inputs[0]] & int(states[inputs[2]])
                elif inputs[1] == "OR":
                    states[output] = states[inputs[0]] | int(states[inputs[2]])
                elif inputs[1] == "XOR":
                    states[output] = states[inputs[0]] ^ int(states[inputs[2]])

        total = ""
        complete = True
        for i in range(answer_length):
            add_zero = "" if i // 10 else "0"
            key = "z" + add_zero + str(i)
            if key in states:
                total = str(states[key]) + total
            else:
                complete = False
                break

        if complete:
            print(int(total, 2))
            return


if __name__ == "__main__":
    main()
