min_total = float("inf")


def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    global min_total
    history = {}

    take_step(1, len(lines[0]) - 3, 1, 0, lines, 1, history)

    print(min_total)


def take_step(x_pos, y_pos, x_dir, y_dir, lines, total, history):
    global min_total
    key = f"{x_pos} {y_pos} {x_dir} {y_dir}"
    if key in history and history[key] <= total:
        return
    history[key] = total

    if lines[y_pos + y_dir][x_pos + x_dir] == "E":
        min_total = min(min_total, total)
        return

    if lines[y_pos + y_dir][x_pos + x_dir] == ".":
        take_step(x_pos + x_dir, y_pos + y_dir, x_dir, y_dir, lines, total + 1, history)

    x_dir_r, y_dir_r = turn_right(x_dir, y_dir)
    take_step(x_pos, y_pos, x_dir_r, y_dir_r, lines, total + 1000, history)
    x_dir, y_dir = turn_left(x_dir, y_dir)
    take_step(x_pos, y_pos, x_dir, y_dir, lines, total + 1000, history)


def turn_right(x_dir, y_dir):
    if x_dir == 1:
        return 0, 1
    elif y_dir == 1:
        return -1, 0
    elif x_dir == -1:
        return 0, -1
    elif y_dir == -1:
        return 1, 0


def turn_left(x_dir, y_dir):
    if x_dir == 1:
        return 0, -1
    elif y_dir == 1:
        return 1, 0
    elif x_dir == -1:
        return 0, 1
    elif y_dir == -1:
        return -1, 0


if __name__ == "__main__":
    main()
