import re


def part1(file):
    dataset = [re.split(" +", item.strip()) for item in open(file, "r").readlines()]
    ops = dataset[-1]
    numbers = dataset[:-1]
    numbers = [list(map(int, row)) for row in numbers]

    total = 0
    for j in range(len(numbers[0])):
        col_result = 0
        op = ops[j]
        if op == "*":
            col_result = 1
        for i in range(len(numbers)):
            if op == "*":
                col_result *= numbers[i][j]
            else:
                col_result += numbers[i][j]
        total += col_result
    print("Result part1:", total)


def part2(file):
    # Load data
    dataset = [list(item)[:-1] for item in open(file, "r").readlines()]
    ops = re.split(" +", "".join(dataset[-1]))[:-1]

    # Reverse the ops due to tranpose of the rest of the dataset:
    ops = list(reversed(ops))
    numbers = dataset[:-1]
    numbers = transpose(numbers)

    # Process thed data per 'block' (an empty column)
    block = []
    grand_total = 0
    for i, row in enumerate(numbers):
        if all(x == " " for x in row):
            op = ops.pop()
            grand_total += process_block(block, op)
            block = []
        else:
            block.append(row)

    # Last block
    op = ops.pop()
    grand_total += process_block(block, op)

    print("Result part2:", grand_total)


def transpose(data):
    data = [[row[i] for row in data] for i in range(len(data[0]))]
    return data


def process_block(block, op):
    # Given a block (2d list) and an op:
    res = 0
    if op == "*":
        res = 1
    for item in block:
        if op == "*":
            res *= int("".join(item))
        else:
            res += int("".join(item))
    return res


def main():
    part1("big.txt")
    part2("big.txt")


if __name__ == "__main__":
    main()
