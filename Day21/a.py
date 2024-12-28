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

        arrows_1 = ""

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
                    arrows_1 += (
                        "^" * difference_y
                        + "<" * difference_x
                        + ">" * (-difference_x)
                        + "v" * (-difference_y)
                        + "A"
                    )
                else:
                    arrows_1 += (
                        "^" * difference_y
                        + "<" * difference_x
                        + "v" * (-difference_y)
                        + ">" * (-difference_x)
                        + "A"
                    )

            else:
                if y == 3:
                    arrows_1 += (
                        "<" * difference_x
                        + "^" * difference_y
                        + ">" * (-difference_x)
                        + "v" * (-difference_y)
                        + "A"
                    )
                else:
                    arrows_1 += (
                        "<" * difference_x
                        + "^" * difference_y
                        + "v" * (-difference_y)
                        + ">" * (-difference_x)
                        + "A"
                    )

            arm_x = x
            arm_y = y

        print(arrows_1)

        arm_x = 2
        arm_y = 0

        arrows_2 = ""

        for char in arrows_1:
            if char == "<":
                x = 0
                y = 1
            elif char == ">":
                x = 2
                y = 1
            elif char == "^":
                x = 1
                y = 0
            elif char == "v":
                x = 1
                y = 1
            elif char == "A":
                x = 2
                y = 0

            difference_x = arm_x - x
            difference_y = arm_y - y

            arm_x = x
            arm_y = y

            arrows_2 += (
                "v" * (-difference_y)
                + "<" * difference_x
                + ">" * (-difference_x)
                + "^" * difference_y
                + "A"
            )

        arm_x = 2
        arm_y = 0

        print(arrows_2)

        arrows_3 = ""

        for char in arrows_2:
            if char == "<":
                x = 0
                y = 1
            elif char == ">":
                x = 2
                y = 1
            elif char == "^":
                x = 1
                y = 0
            elif char == "v":
                x = 1
                y = 1
            elif char == "A":
                x = 2
                y = 0

            difference_x = arm_x - x
            difference_y = arm_y - y

            arm_x = x
            arm_y = y

            arrows_3 += (
                "v" * (-difference_y)
                + "<" * difference_x
                + ">" * (-difference_x)
                + "^" * difference_y
                + "A"
            )

        print(arrows_3)
        print(len(arrows_3))
        print(len(arrows_3), int(code[:-1]))

        total += len(arrows_3) * int(code[:-1])

    print(total)


if __name__ == "__main__":
    main()
