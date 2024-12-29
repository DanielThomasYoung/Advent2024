def main() -> int:
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    total = set()
    connections = {}

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

    for key, value in connections.items():
        if key[0] != "t":
            continue

        for connection in value:
            for other_connection in connections[connection]:
                if key in connections[other_connection]:
                    triple = [key, connection, other_connection]
                    triple.sort()
                    total.add(str(triple))

    print(len(total))


if __name__ == "__main__":
    main()
