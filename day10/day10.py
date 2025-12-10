from itertools import combinations
from pprint import pprint


def part2(dataset):
    pass


def parse_input(file):
    dataset = [item.strip().split(" ") for item in open(file, "r").readlines()]

    entries = []
    for row in dataset:
        entry = {}
        # Diagram
        # .##. / 0110
        # First block
        diagram = tuple(x == "#" for x in list(row.pop(0)[1:-1]))

        # Required Joltages (unused for part1)
        # {3,5,4,7}
        # Last block
        joltage = list(map(int, row.pop()[1:-1].split(",")))

        # Wiring schematics
        # (3) (1,3) (2) (2,3) (0,2) (0,1)
        # Middle stuff:
        wirings = []
        for item in row:
            wiring = [False] * len(diagram)
            for x in map(int, item[1:-1].split(",")):
                wiring[x] = True
            wirings.append(wiring)
        entry["diagram"] = diagram
        entry["joltage"] = joltage
        entry["wirings"] = wirings
        entries.append(entry)

    return entries


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def part1(entries):
    solution = []

    for entry in entries:
        result = None
        for n in range(1, len(entry["wirings"]) + 1):
            if result:
                solution.append(result)
                break
            button_options = list(combinations(entry["wirings"], n))

            for buttons in button_options:
                current = tuple([False] * len(entry["diagram"]))
                for button in buttons:
                    current = xor(current, button)
                if current == entry["diagram"]:
                    result = n
    print("Solution part1:", sum(solution))


def main():
    entries = parse_input("big.txt")
    part1(entries)


if __name__ == "__main__":
    main()
