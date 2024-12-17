from dataclasses import dataclass


def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    positions = [Position(1, len(lines) - 2, 1, 0, 1)]
    history = {}

    while True:
        cur = min(positions, key=lambda pos: pos.distance)
        key = f"{cur.pos_x} {cur.pos_y} {cur.dir_x} {cur.dir_y}"
        if key in history and history[key] <= cur.distance:
            positions.remove(cur)
            continue
        history[key] = cur.distance

        forward = lines[cur.pos_y + cur.dir_y][cur.pos_x + cur.dir_x]

        if forward == "E":
            print(cur.distance)
            return

        if forward == ".":
            new = Position(
                cur.pos_x + cur.dir_x,
                cur.pos_y + cur.dir_y,
                cur.dir_x,
                cur.dir_y,
                cur.distance + 1,
            )

            match = False
            for pos in positions:
                if (
                    pos.pos_x == new.pos_x
                    and pos.pos_y == new.pos_y
                    and pos.dir_x == new.dir_x
                    and pos.dir_y == new.dir_y
                ):
                    pos.distance = min(pos.distance, new.distance)
                    match = True
                    break

            if not match:
                positions.append(new)

        x_dir, y_dir = turn_right(cur.dir_x, cur.dir_y)
        if lines[cur.pos_y + y_dir][cur.pos_x + x_dir] != "#":
            new = Position(cur.pos_x, cur.pos_y, x_dir, y_dir, cur.distance + 1000)

            match = False
            for pos in positions:
                if (
                    pos.pos_x == new.pos_x
                    and pos.pos_y == new.pos_y
                    and pos.dir_x == new.dir_x
                    and pos.dir_y == new.dir_y
                ):
                    pos.distance = min(pos.distance, new.distance)
                    match = True
                    break

            if not match:
                positions.append(new)

        x_dir, y_dir = turn_left(cur.dir_x, cur.dir_y)
        if lines[cur.pos_y + y_dir][cur.pos_x + x_dir] != "#":
            new = Position(cur.pos_x, cur.pos_y, x_dir, y_dir, cur.distance + 1000)

            match = False
            for pos in positions:
                if (
                    pos.pos_x == new.pos_x
                    and pos.pos_y == new.pos_y
                    and pos.dir_x == new.dir_x
                    and pos.dir_y == new.dir_y
                ):
                    pos.distance = min(pos.distance, new.distance)
                    match = True
                    break

            if not match:
                positions.append(new)

        positions.remove(cur)


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


@dataclass
class Position:
    pos_x: int
    pos_y: int
    dir_x: int
    dir_y: int
    distance: int


if __name__ == "__main__":
    main()
