import re


def main() -> int:
    with open("input.txt", "r") as file:
        all_lines = file.readlines()

    width = 101
    height = 103

    quadrants = [0, 0, 0, 0]
    for line in all_lines:
        match = re.match(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", line)
        p_x, p_y, v_x, v_y = map(int, match.groups())

        final_x = (p_x + 100 * v_x) % width
        final_y = (p_y + 100 * v_y) % height

        if final_x < width // 2 and final_y < height // 2:
            quadrants[0] += 1
        elif final_x < width // 2 and final_y > height // 2:
            quadrants[1] += 1
        elif final_x > width // 2 and final_y < height // 2:
            quadrants[2] += 1
        elif final_x > width // 2 and final_y > height // 2:
            quadrants[3] += 1

    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


if __name__ == "__main__":
    main()
