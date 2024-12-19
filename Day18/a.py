from dataclasses import dataclass


def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    lines = [["#"] * 73]
    for _ in range(71):
        lines.append(["#"] + ["."] * 71 + ["#"])
    lines.append(["#"] * 73)

    line_number = 0
    for line in file_lines:
        if line_number == 1024:
            break
        coords = line.split(",")
        lines[int(coords[0]) + 1][int(coords[1]) + 1] = "#"
        line_number += 1

    positions = [Position(1, 1, 0)]
    history = set()

    while positions:
        cur = min(positions, key=lambda pos: pos.distance)
        positions.remove(cur)
        if cur.pos_x == len(lines) - 2 and cur.pos_y == len(lines) - 2:
            print(cur.distance)
            return

        key = f"{cur.pos_x} {cur.pos_y}"
        if key in history:
            continue
        history.add(key)

        if lines[cur.pos_x + 1][cur.pos_y] != "#":
            positions.append(Position(cur.pos_x + 1, cur.pos_y, cur.distance + 1))

        if lines[cur.pos_x][cur.pos_y + 1] != "#":
            positions.append(Position(cur.pos_x, cur.pos_y + 1, cur.distance + 1))

        if lines[cur.pos_x - 1][cur.pos_y] != "#":
            positions.append(Position(cur.pos_x - 1, cur.pos_y, cur.distance + 1))

        if lines[cur.pos_x][cur.pos_y - 1] != "#":
            positions.append(Position(cur.pos_x, cur.pos_y - 1, cur.distance + 1))


@dataclass
class Position:
    pos_x: int
    pos_y: int
    distance: int


if __name__ == "__main__":
    main()
