import re
from time import sleep


def main() -> int:
    with open("input.txt", "r") as file:
        all_lines = file.readlines()

    width = 101
    height = 103

    robots = []

    lines = []
    for _ in range(height):
        lines.append([" "] * width)

    i = 7138

    for line in all_lines:
        match = re.match(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", line)
        p_x, p_y, v_x, v_y = map(int, match.groups())
        # robots.append([p_x, p_y, v_x, v_y])
        lines[(p_y + i * v_y) % height][(p_x + i * v_x) % width] = "*"

    # for robot in robots:
    #     robot[0] = (robot[0] + 7137 * robot[2]) % width
    #     robot[1] = (robot[1] + 7137 * robot[3]) % height

    # count = 0
    # while True:
    #     lines = []
    #     for _ in range(height):
    #         lines.append([" "] * width)

    #     for robot in robots:
    #         robot[0] = (robot[0] + robot[2]) % width
    #         robot[1] = (robot[1] + robot[3]) % height

    #         lines[robot[1]][robot[0]] = "*"

    for row in lines:
        print("".join(row))
    #     print(count)

    #     sleep(.5)

    #     count += 1


if __name__ == "__main__":
    main()


# 7137 too low
