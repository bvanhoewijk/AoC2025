import numpy as np


def part1(dataset):
    item = dataset[0]

    result = 0
    for item in dataset:
        first = np.argmax(item)
        if first != len(item) - 1:
            second = np.argmax(item[(first + 1) :])
            # print(str(item[first]) + str(item[(first+1):][second]))
            result += int(str(item[first]) + str(item[(first + 1) :][second]))
        else:
            item = item[::-1]
            first = np.argmax(item)
            second = np.argmax(item[(first + 1) :])
            # print(str(item[(first+1):][second]) + str(item[first]))
            result += int(str(item[(first + 1) :][second]) + str(item[first]))
    print(f"Solution part 1: {result}")


def part2(dataset):

    # For a bank of size n (so line length) and m batteries:
    # Find the biggest digit in the first n-m+1 digits of the bank at position k. This is your first battery.
    # Now solve the same problem with the substring of the bank starting at k+1. This substring has at least m-1 characters.
    # Repeat until you have all your batteries.

    bank_len = len(dataset[0])

    sum = 0
    for bank in dataset:
        joltage = []
        bestkey = -1

        for battery in range(12):
            bestval = 0
            k = bestkey + 1
            while k < (bank_len + 1 - 12 + battery) and bestval < 9:
                if bank[k] > bestval:
                    bestkey = k
                    bestval = bank[k]
                k += 1
            joltage.append(bestval)
        sum += int("".join(list(map(str, joltage))))
    print(f"Solution part 2: {sum}")


def main():
    dataset = [
        list(map(int, list(x.strip()))) for x in open("big.txt", "r").readlines()
    ]
    part1(dataset)
    part2(dataset)


if __name__ == "__main__":
    main()
