from itertools import combinations


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
                results["correction"] = 0
                results["perimeter"] = set()
                results["perimeter"].add((line_index + 0.5, char_index))
                results["perimeter"].add((line_index - 0.5, char_index))
                results["perimeter"].add((line_index, char_index + 0.5))
                results["perimeter"].add((line_index, char_index - 0.5))
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

                    parameter = len(results["perimeter"])

                    for item1, item2 in combinations(results["perimeter"], 2):
                        if (
                            item1[0] % 1 == 0.5
                            and item1[0] == item2[0]
                            and abs(item1[1] - item2[1]) == 1
                        ):
                            parameter -= 1
                        elif (
                            item1[1] % 1 == 0.5
                            and item1[1] == item2[1]
                            and abs(item1[0] - item2[0]) == 1
                        ):
                            parameter -= 1

                    total += results["area"] * (parameter + results["correction"])

    print(total)


def check_adjacents(
    char, lines, line_index, char_index, previously_checked, currently_checking, results
):
    # correcting for the lack of Möbius Fencing
    if (
        str(f"{line_index-1} {char_index-1}") in currently_checking
        and char != lines[line_index - 1][char_index]
        and char != lines[line_index][char_index - 1]
    ):
        results["correction"] += 2
    if (
        str(f"{line_index-1} {char_index+1}") in currently_checking
        and char != lines[line_index - 1][char_index]
        and char != lines[line_index][char_index + 1]
    ):
        results["correction"] += 2
    if (
        str(f"{line_index+1} {char_index-1}") in currently_checking
        and char != lines[line_index + 1][char_index]
        and char != lines[line_index][char_index - 1]
    ):
        results["correction"] += 2
    if (
        str(f"{line_index+1} {char_index+1}") in currently_checking
        and char != lines[line_index + 1][char_index]
        and char != lines[line_index][char_index + 1]
    ):
        results["correction"] += 2
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
            results["perimeter"].add((adj_line_index + 0.5, adj_char_index))
            results["perimeter"].add((adj_line_index - 0.5, adj_char_index))
            results["perimeter"].add((adj_line_index, adj_char_index + 0.5))
            results["perimeter"].add((adj_line_index, adj_char_index - 0.5))
            for perimeter_line, perimeter_char in [
                (adj_line_index + 1, adj_char_index),
                (adj_line_index - 1, adj_char_index),
                (adj_line_index, adj_char_index + 1),
                (adj_line_index, adj_char_index - 1),
            ]:
                midpoint = (
                    (perimeter_line + adj_line_index) / 2,
                    (perimeter_char + adj_char_index) / 2,
                )
                if (
                    str(f"{perimeter_line} {perimeter_char}") in currently_checking
                    and midpoint in results["perimeter"]
                ):
                    results["perimeter"].remove(midpoint)
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
