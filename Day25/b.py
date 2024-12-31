from copy import deepcopy
from itertools import combinations


def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    connections = {}
    connected = True

    for line in file_lines:
        chars = line.strip().split("-")
        if chars[0] in connections:
            connections[chars[0]].append(chars[1])
        else:
            connections[chars[0]] = [chars[1]]

        if chars[1] in connections:
            connections[chars[1]].append(chars[0])
        else:
            connections[chars[1]] = [chars[0]]

    count = 3
    while True:
        for key, value in connections.items():
            groups = list(combinations(value, count))
            connected = True

            for group in groups:
                group = list(group)
                copy = deepcopy(group)

                group_a = group.pop()
                while group and connected:
                    for group_b in group:
                        if group_b not in connections[group_a]:
                            connected = False
                    group_a = group.pop()

                if connected:
                    copy.append(key)
                    copy.sort()
                    print(copy)
                    break

            if connected:
                break

        if connected:
            count += 1
        else:
            break


if __name__ == "__main__":
    main()
