#!/usr/bin/env python3
import re
from pprint import pprint


def parse_input(file):
    dataset = "".join([item for item in open(file, "r").readlines()])
    dataset = dataset.split("\n\n")

    shapes = []
    for shape in dataset[:-1]:
        coordinates = []
        for r, row in enumerate(shape.split("\n")[1:]):
            for c, col in enumerate(list(row)):
                if col == "#":
                    coordinates.append((r, c))
        shapes.append({"coords": coordinates, "size": len(coordinates)})

    parsed_regions = []
    for region in dataset[-1].split("\n"):
        # Tuple and List:
        # ((4, 4), [0, 0, 0, 0, 2, 0])
        a = re.search(r"(^\d+)x(\d+): (.+)", region)
        parsed_regions.append(
            ((int(a.group(1)), int(a.group(2))), list(map(int, a.group(3).split(" "))))
        )

    return shapes, parsed_regions


def part1(shapes, regions):
    res = 0
    for region in regions:
        print(region)
        total_present_area = 0
        available_area, presents = region
        for i, x in enumerate(presents):
            if x > 0:
                total_present_area += shapes[i]["size"] * x
        res += available_area[0] * available_area[1] > total_present_area
    print(res)


def part2(dataset):
    pass


def main():
    shapes, regions = parse_input("big.txt")
    part1(shapes, regions)


if __name__ == "__main__":
    main()
