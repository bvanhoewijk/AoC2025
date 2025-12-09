from itertools import combinations

def part2(dataset):
    pass

def calc_area(a, b):
    xlen = abs(a[0] - b[0]) + 1
    ylen = abs(a[1] - b[1]) + 1
    return xlen * ylen

def part1(dataset):
    result = max([calc_area(a,b) for a, b in combinations(dataset, 2)])
    
    print("Solution part1:", result)

def main():
    dataset = [tuple(map(eval, item.split(","))) for item in open("big.txt", "r").readlines()]
    print(len(list(combinations(dataset, 2))))
    part1(dataset)

if __name__ == "__main__":
    main()