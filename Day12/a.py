def main() -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    padded_line = ["." * (len(lines[0]) + 2)]
    for line in lines:
        padded_line.append("." + line.strip() + ".")
    padded_line.append("." * (len(lines[0]) + 2))
    lines = padded_line

    total = 0
    previously_checked = set()
    results = {}

    for line_index in range(len(lines)):
        for char_index in range(len(lines[line_index])):
            if str(f"{line_index} {char_index}") not in previously_checked:
                results["area"] = 1
                results["perimeter"] = 4
                char = lines[line_index][char_index]
                if char != ".":
                    previously_checked.add(str(f"{line_index} {char_index}"))
                    currently_checking = set([str(f"{line_index} {char_index}")])
                    check_adjacents(
                        char,
                        lines,
                        line_index,
                        char_index,
                        previously_checked,
                        currently_checking,
                        results,
                    )
                    total += results["area"] * results["perimeter"]

    print(total)


def check_adjacents(
    char, lines, line_index, char_index, previously_checked, currently_checking, results
):
    for adj_line_index, adj_char_index in [
        (line_index + 1, char_index),
        (line_index - 1, char_index),
        (line_index, char_index + 1),
        (line_index, char_index - 1),
    ]:
        if (
            lines[adj_line_index][adj_char_index] == char
            and str(f"{adj_line_index} {adj_char_index}") not in previously_checked
        ):
            results["area"] += 1
            results["perimeter"] += 4
            for perimeter_line, perimeter_char in [
                (adj_line_index + 1, adj_char_index),
                (adj_line_index - 1, adj_char_index),
                (adj_line_index, adj_char_index + 1),
                (adj_line_index, adj_char_index - 1),
            ]:
                if str(f"{perimeter_line} {perimeter_char}") in currently_checking:
                    results["perimeter"] -= 2
            previously_checked.add(str(f"{adj_line_index} {adj_char_index}"))
            currently_checking.add(str(f"{adj_line_index} {adj_char_index}"))
            check_adjacents(
                char,
                lines,
                adj_line_index,
                adj_char_index,
                previously_checked,
                currently_checking,
                results,
            )


if __name__ == "__main__":
    main()
