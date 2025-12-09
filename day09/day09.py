from itertools import combinations
from shapely.geometry import Polygon, box


def calc_area(a, b):
    xlen = abs(a[0] - b[0]) + 1
    ylen = abs(a[1] - b[1]) + 1
    return xlen * ylen


def part1(dataset):
    result = max([calc_area(a, b) for a, b in combinations(dataset, 2)])

    print("Solution part1:", result)


def min_max(a, b):
    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])
    return min_x, min_y, max_x, max_y


def part2(dataset):
    polygon = Polygon(dataset)

    max_area = 0
    for a, b in combinations(dataset, 2):
        m = calc_area(a, b)
        if m < max_area:
            continue
        rectangle = box(*min_max(a, b))
        if polygon.contains(rectangle):
            if m >= max_area:
                max_area = m

    print("Solution part2:", max_area)


def main():
    dataset = [
        tuple(map(eval, item.split(","))) for item in open("big.txt", "r").readlines()
    ]
    part1(dataset)
    part2(dataset)


if __name__ == "__main__":
    main()
