def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()
    total = 0
    needed_char = ["m", "u", "l", "("]

    progress = 0
    multiplying = False
    reading_first_number = True
    first_number = 0
    second_number = 0

    for line in lines:
        for char in line:
            if multiplying:
                if char == ",":
                    reading_first_number = False

                elif char.isdigit():
                    if reading_first_number:
                        first_number = first_number * 10 + int(char)
                    else:
                        second_number = second_number * 10 + int(char)

                elif char == ")":
                    total += first_number * second_number
                    reading_first_number = True

                    progress = 0
                    multiplying = False
                    reading_first_number = True
                    first_number = 0
                    second_number = 0

                else:
                    progress = 0
                    multiplying = False
                    reading_first_number = True
                    first_number = 0
                    second_number = 0

            else:
                if char == needed_char[progress]:
                    progress += 1
                    if progress == 4:
                        progress = 0
                        multiplying = True

    print(total)


if __name__ == "__main__":
    main()
