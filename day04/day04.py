directions = [
    [0, -1],  # up
    [1, -1],  # up right
    [1, 0],  # right
    [1, 1],  # down right
    [0, 1],  # down
    [-1, 1],  # down left
    [-1, 0],  # left
    [-1, -1],  # left up
]


def part1(dataset):
    all_rolls = set()

    # Store all "@" in a set of coordinates:
    for r in range(len(dataset)):
        for c in range(len(dataset[0])):
            if dataset[r][c] == "@":
                all_rolls.add((r, c))

    result = set()
    for r, c in all_rolls:
        paper_rolls = 0
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if (nr, nc) in all_rolls:
                paper_rolls += 1

        if paper_rolls < 4:
            result.add((r, c))

    print(f"Result part 1: {len(result)}")


def part2(dataset):
    # Init:
    all_rolls = set()

    # Store all "@" in a set of coordinates:
    for r in range(len(dataset)):
        for c in range(len(dataset[0])):
            if dataset[r][c] == "@":
                all_rolls.add((r, c))

    all_removed = 0
    while True:
        result = set()
        for r, c in all_rolls:
            paper_rolls = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr, nc) in all_rolls:
                    paper_rolls += 1

            if paper_rolls < 4:
                result.add((r, c))

        # No more rolls to remove. Break out:
        if not len(result):
            break

        # Add the number of rolls removed
        all_removed += len(result)
        for r in result:
            all_rolls.remove(r)

    print(f"Result part 2: {all_removed}")


def main():
    dataset = [[x for x in item.strip()] for item in open("big.txt", "r").readlines()]
    part1(dataset)
    part2(dataset)


if __name__ == "__main__":
    main()
