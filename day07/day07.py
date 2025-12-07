def part1(dataset):
    # Find start
    start = dataset[0].index("S")
    start = (0, start)

    queue = set()
    queue.add(start)

    split = set()
    path = set()
    while queue:
        r, c = queue.pop()
        if r + 1 < len(dataset):
            if dataset[r + 1][c] == ".":
                queue.add((r + 1, c))
                path.add((r + 1, c))
            else:
                split.add((r, c))
                queue.add((r + 1, c - 1))
                queue.add((r + 1, c + 1))
                path.add((r + 1, c - 1))
                path.add((r + 1, c + 1))

    # Print path
    for r, row in enumerate(dataset):
        for c, col in enumerate(row):
            if (r, c) in path:
                print("|", end="")
            else:
                print(dataset[r][c], end="")
        print()
    print()
    print("Solution part 1", len(split))


def part2(dataset):
    # Find Start
    start = dataset[0].index("S")

    num_cols = len(dataset[0])
    num_rows = len(dataset)

    score = [0] * num_cols
    score[start] = 1

    # Start at second row
    for r in range(1, num_rows):
        new_score = [0] * num_cols

        for c in range(num_cols):
            old_value = score[c]

            if old_value == 0:
                # Nothing to do
                continue

            if dataset[r][c] == ".":
                # Just straight down. Add previous 'paths'
                new_score[c] += old_value
            elif dataset[r][c] == "^":
                # Split paths and add:
                new_score[c - 1] += old_value
                new_score[c + 1] += old_value
        score = new_score
    print("Solution part 2", sum(score))


def main():
    dataset = [list(item.strip()) for item in open("big.txt", "r").readlines()]

    part1(dataset)
    part2(dataset)


if __name__ == "__main__":
    main()
