from dataclasses import dataclass


def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    positions = [Position(1, len(lines) - 2, 1, 0, 1, set())]
    global_history = {}
    end = []  # distance, length

    while positions:
        cur = min(positions, key=lambda pos: pos.distance)
        key = f"{cur.pos_x} {cur.pos_y} {cur.dir_x} {cur.dir_y}"
        if key in global_history and global_history[key] < cur.distance:
            positions.remove(cur)
            continue
        global_history[key] = cur.distance

        cur.history.add(f"{cur.pos_x} {cur.pos_y}")
        forward = lines[cur.pos_y + cur.dir_y][cur.pos_x + cur.dir_x]

        if forward == "E":
            if end:
                if end[0] == cur.distance:
                    end[1] += len(cur.history)
                else:
                    print(end[1] + 1)
                    break
            else:
                end.append(cur.distance)
                end.append(len(cur.history))

        if forward == ".":
            new = Position(
                cur.pos_x + cur.dir_x,
                cur.pos_y + cur.dir_y,
                cur.dir_x,
                cur.dir_y,
                cur.distance + 1,
                cur.history.copy(),
            )

            match = False
            for pos in positions:
                if (
                    pos.pos_x == new.pos_x
                    and pos.pos_y == new.pos_y
                    and pos.dir_x == new.dir_x
                    and pos.dir_y == new.dir_y
                ):
                    if pos.distance == new.distance:
                        pos.history.update(cur.history)
                    match = True
                    break

            if not match:
                positions.append(new)

        x_dir, y_dir = turn_right(cur.dir_x, cur.dir_y)
        if lines[cur.pos_y + y_dir][cur.pos_x + x_dir] != "#":
            new = Position(
                cur.pos_x,
                cur.pos_y,
                x_dir,
                y_dir,
                cur.distance + 1000,
                cur.history.copy(),
            )

            match = False
            for pos in positions:
                if (
                    pos.pos_x == new.pos_x
                    and pos.pos_y == new.pos_y
                    and pos.dir_x == new.dir_x
                    and pos.dir_y == new.dir_y
                ):
                    if pos.distance == new.distance:
                        pos.history.update(cur.history)
                    match = True
                    break

            if not match:
                positions.append(new)

        x_dir, y_dir = turn_left(cur.dir_x, cur.dir_y)
        if lines[cur.pos_y + y_dir][cur.pos_x + x_dir] != "#":
            new = Position(
                cur.pos_x,
                cur.pos_y,
                x_dir,
                y_dir,
                cur.distance + 1000,
                cur.history.copy(),
            )

            match = False
            for pos in positions:
                if (
                    pos.pos_x == new.pos_x
                    and pos.pos_y == new.pos_y
                    and pos.dir_x == new.dir_x
                    and pos.dir_y == new.dir_y
                ):
                    if pos.distance == new.distance:
                        pos.history.update(cur.history)
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
    history: set


if __name__ == "__main__":
    main()
