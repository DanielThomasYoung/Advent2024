from dataclasses import dataclass


def main() -> int:
    with open("input.txt", "r") as file:
        lines = [["#"] * 73]
        for _ in range(71):
            lines.append(["#"] + ["."] * 71 + ["#"])
        lines.append(["#"] * 73)

        found = True
        path = set()
        while found:
            coords = file.readline().strip().split(",")
            lines[int(coords[0]) + 1][int(coords[1]) + 1] = "#"

            if path and f"{int(coords[0]) + 1} {int(coords[1]) + 1}" not in path:
                continue

            found = False
            positions = [Position(1, 1, 0, set())]
            history = set()
            while positions:
                cur = min(positions, key=lambda pos: pos.distance)
                positions.remove(cur)
                if cur.pos_x == len(lines) - 2 and cur.pos_y == len(lines) - 2:
                    found = True
                    path = cur.history
                    break

                key = f"{cur.pos_x} {cur.pos_y}"
                cur.history.add(key)
                if key in history:
                    continue
                history.add(key)

                if lines[cur.pos_x + 1][cur.pos_y] != "#":
                    positions.append(
                        Position(
                            cur.pos_x + 1,
                            cur.pos_y,
                            cur.distance + 1,
                            cur.history.copy(),
                        )
                    )

                if lines[cur.pos_x][cur.pos_y + 1] != "#":
                    positions.append(
                        Position(
                            cur.pos_x,
                            cur.pos_y + 1,
                            cur.distance + 1,
                            cur.history.copy(),
                        )
                    )

                if lines[cur.pos_x - 1][cur.pos_y] != "#":
                    positions.append(
                        Position(
                            cur.pos_x - 1,
                            cur.pos_y,
                            cur.distance + 1,
                            cur.history.copy(),
                        )
                    )

                if lines[cur.pos_x][cur.pos_y - 1] != "#":
                    positions.append(
                        Position(
                            cur.pos_x,
                            cur.pos_y - 1,
                            cur.distance + 1,
                            cur.history.copy(),
                        )
                    )

        print(coords)


@dataclass
class Position:
    pos_x: int
    pos_y: int
    distance: int
    history: set


if __name__ == "__main__":
    main()
