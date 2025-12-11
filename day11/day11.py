#!/usr/bin/env python3
from collections import deque
from functools import cache
from pprint import pprint


def parse_input(file):
    dataset = [item.strip() for item in open(file, "r").readlines()]
    cables = dict()
    for item in dataset:
        key = item.split(": ")[0]
        value = item.split(": ")[1].split(" ")
        cables[key] = value
    return cables


# 390108778818526
def part2(dataset):
    @cache
    def dfs(node, dac, fft):
        if node == "out":
            return dac and fft

        paths = 0
        for destination in dataset[node]:
            paths += dfs(
                destination, dac | (destination == "dac"), fft | (destination == "fft")
            )
        return paths

    print("Solution part2:", dfs("svr", False, False))


def part1(dataset):
    start = "you"
    queue = list()

    queue.append(([start], start))
    paths = []
    while len(queue):
        path, node = queue.pop(0)

        if node == "out":
            paths.append(path)
        else:
            for item in dataset[node]:
                path.append(item)
                queue.append((path.copy(), item))
    print("Solution part1:", len(paths))


def main():
    # part1(dataset)
    dataset = parse_input("big.txt")
    dataset = parse_input("big.txt")
    part1(dataset)
    part2(dataset)


if __name__ == "__main__":
    main()
