def main() -> int:
    with open("input.txt", "r") as file:
        line = file.readline()

    stones = {stone: 1 for stone in line.strip().split()}

    for _ in range(1000):
        stones = blink(stones)

    print(sum(stones.values()))


def blink(stones):
    new_stones = {}
    for key, value in stones.items():
        if key == "0":
            new_stones["1"] = new_stones.get("1", 0) + value
        elif len(key) % 2 == 0:
            midpoint = len(key) // 2
            first_half = str(int(key[:midpoint]))
            second_half = str(int(key[midpoint:]))
            new_stones[first_half] = new_stones.get(first_half, 0) + value
            new_stones[second_half] = new_stones.get(second_half, 0) + value
        else:
            multiplied_key = str(int(key) * 2024)
            new_stones[multiplied_key] = new_stones.get(multiplied_key, 0) + value

    return new_stones


if __name__ == "__main__":
    main()
