def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    total = 0

    for code in file_lines:
        code = code.strip()
        arm_x = 2
        arm_y = 3

        x = 0
        y = 0

        arrows = {}

        for char in code:
            if char == "0":
                x = 1
                y = 3
            elif char == "1":
                x = 0
                y = 2
            elif char == "2":
                x = 1
                y = 2
            elif char == "3":
                x = 2
                y = 2
            elif char == "4":
                x = 0
                y = 1
            elif char == "5":
                x = 1
                y = 1
            elif char == "6":
                x = 2
                y = 1
            elif char == "7":
                x = 0
                y = 0
            elif char == "8":
                x = 1
                y = 0
            elif char == "9":
                x = 2
                y = 0
            elif char == "A":
                x = 2
                y = 3

            difference_x = arm_x - x
            difference_y = arm_y - y

            if arm_y == 3:
                if y == 3:
                    pattern = (
                        "^" * difference_y
                        + "<" * difference_x
                        + ">" * (-difference_x)
                        + "v" * (-difference_y)
                        + "A"
                    )
                else:
                    pattern = (
                        "^" * difference_y
                        + "<" * difference_x
                        + "v" * (-difference_y)
                        + ">" * (-difference_x)
                        + "A"
                    )

            else:
                if y == 3:
                    pattern = (
                        "<" * difference_x
                        + "^" * difference_y
                        + ">" * (-difference_x)
                        + "v" * (-difference_y)
                        + "A"
                    )
                else:
                    pattern = (
                        "<" * difference_x
                        + "^" * difference_y
                        + "v" * (-difference_y)
                        + ">" * (-difference_x)
                        + "A"
                    )

            if pattern in arrows:
                arrows[pattern] += 1
            else:
                arrows[pattern] = 1

            arm_x = x
            arm_y = y

        print(arrows)

        for i in range(25):
            src = "A"

            next_arrows = {}

            for group, count in arrows.items():
                for char in group:
                    pattern = get_paths(src, char) + "A"
                    src = char

                    if pattern in next_arrows:
                        next_arrows[pattern] += count
                    else:
                        next_arrows[pattern] = count
            arrows = next_arrows
            print(arrows)
            print(i)

        complexity = 0
        for group, count in arrows.items():
            complexity += len(group) * count
        total += complexity * int(code[:-1])

    print(total)


def get_paths(src, dst):
    print("get_paths")
    print(src, dst)
    if src == dst:
        return ""

    if src == "<" and dst == "^":
        return ">^"
    elif src == "<" and dst == "A":
        return ">>^"
    elif src == "<" and dst == "v":
        return ">"
    elif src == "<" and dst == ">":
        return ">>"

    elif src == "^" and dst == "<":
        return "v<"
    elif src == "^" and dst == "A":
        return ">"
    elif src == "^" and dst == "v":
        return "v"
    elif src == "^" and dst == ">":
        return "v>"

    elif src == "A" and dst == "<":
        return "v<<"
    elif src == "A" and dst == "^":
        return "<"
    elif src == "A" and dst == "v":
        return "<v"
    elif src == "A" and dst == ">":
        return "v"

    elif src == "v" and dst == "<":
        return "<"
    elif src == "v" and dst == "^":
        return "^"
    elif src == "v" and dst == ">":
        return ">"
    elif src == "v" and dst == "A":
        return "^>"

    elif src == ">" and dst == "<":
        return "<<"
    elif src == ">" and dst == "^":
        return "<^"
    elif src == ">" and dst == "v":
        return "<"
    elif src == ">" and dst == "A":
        return "^"


if __name__ == "__main__":
    main()
