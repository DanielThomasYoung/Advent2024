class MultiplicationState:
    def __init__(self):
        self.mul_progress = 0
        self.do_progress = 0
        self.dont_progress = 0
        self.multiplying = False
        self.reading_first_number = True
        self.first_number = 0
        self.second_number = 0

    def clear(self):
        self.mul_progress = 0
        self.do_progress = 0
        self.dont_progress = 0
        self.multiplying = False
        self.reading_first_number = True
        self.first_number = 0
        self.second_number = 0


def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total = 0
    mul_characters = ["m", "u", "l", "("]
    do_characters = ["d", "o", "(", ")"]
    dont_characters = ["d", "o", "n", "'", "t", "(", ")"]
    active = True

    state = MultiplicationState()

    for line in lines:
        for char in line:
            if state.multiplying:
                if char == ",":
                    state.reading_first_number = False
                elif char.isdigit():
                    if state.reading_first_number:
                        state.first_number = state.first_number * 10 + int(char)
                    else:
                        state.second_number = state.second_number * 10 + int(char)
                elif char == ")":
                    total += state.first_number * state.second_number
                    state.clear()
                else:
                    state.clear()
            else:
                if active and char == mul_characters[state.mul_progress]:
                    state.do_progress = 0
                    state.dont_progress = 0
                    state.mul_progress += 1
                    if state.mul_progress == len(mul_characters):
                        state.mul_progress = 0
                        state.multiplying = True
                elif not active and char == do_characters[state.do_progress]:
                    state.mul_progress = 0
                    state.dont_progress = 0
                    state.do_progress += 1
                    if state.do_progress == len(do_characters):
                        state.do_progress = 0
                        active = True
                elif active and char == dont_characters[state.dont_progress]:
                    state.mul_progress = 0
                    state.do_progress = 0
                    state.dont_progress += 1
                    if state.dont_progress == len(dont_characters):
                        state.dont_progress = 0
                        active = False
                else:
                    state.clear()

    print(total)


if __name__ == "__main__":
    main()
