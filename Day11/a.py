def main() -> int:
    with open("input.txt", "r") as file:
        line = file.readline()

    stones = line.strip().split()

    for _ in range(25):
        blink(stones)

    print(len(stones))


def blink(stones):
    for index in range(len(stones) - 1, -1, -1):
        stone = stones[index]
        if stone == "0":
            stones[index] = "1"
        elif len(stone) % 2 == 0:
            midpoint = len(stone) // 2
            first_half = str(int(stone[:midpoint]))
            second_half = str(int(stone[midpoint:]))
            stones[index] = second_half
            stones.insert(index, first_half)
        else:
            stones[index] = str(int(stones[index]) * 2024)


if __name__ == "__main__":
    main()
