import os
import numpy as np


def part1(instructions):
    result = 0
    pointer = 50
    for ins in instructions:
        pointer = (pointer + ins) % 100
        if pointer == 0:
            result += 1
    print("Solution Part1: ", result)


def part2(instructions):
    result = 0
    pointer = 50
    for turn in instructions:
        start_at_zero = pointer != 0
        pointer += turn
        if pointer == 0:
            result += 1
        elif pointer >= 100:
            result += pointer // 100
        elif pointer < 0:
            # Offset:
            result += pointer // -100 + start_at_zero
        pointer = pointer % 100

    print("Solution Part2: ", result)


if __name__ == "__main__":
    lines = open("big.txt", "r").readlines()
    dataset = [(x[0], int(x[1:])) for x in lines]
    instructions = []
    for dir, ins in dataset:
        if dir == "L":
            instructions.append(-ins)
        else:
            instructions.append(ins)
    part1(instructions=instructions)
    part2(instructions=instructions)
