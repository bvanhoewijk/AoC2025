def part1(ingredients, intervals):
    good = []
    for ing in ingredients:
        spoiled = True
        for interval in intervals:
            if ing <= interval[1] and ing >= interval[0]:
                spoiled = False
        if not spoiled:
            good.append(ing)
    print("Solution part1: ", len(good))


def merge_overlap(intervals):
    n = len(intervals)

    intervals.sort()
    result = []

    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]

        # Reach end?
        if result and result[-1][1] >= end:
            continue

        # Find the end of the merged range:
        for j in range(i + 1, n):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
        result.append([start, end])
    return result


def part2(intervals):
    intervals = merge_overlap(intervals)

    interval_sum = 0
    for interval in intervals:
        interval_sum += len(range(interval[0], interval[1] + 1))
    print("Solution part2: ", interval_sum)


def main():
    intervals = []
    first_part = True
    ingredients = []
    for line in open("big.txt", "r").readlines():
        line = line.strip()
        if line:
            if first_part:
                intervals.append(line)
            else:
                ingredients.append(line)
        else:
            first_part = False

    ingredients = [int(x) for x in ingredients]
    intervals = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in intervals]

    part1(ingredients, intervals)
    part2(intervals)


if __name__ == "__main__":
    main()
