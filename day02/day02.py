import re


def part1(dataset):
    invalids = 0
    for item in dataset:
        item_list = list(range(item[0], item[1] + 1))
        for id in item_list:
            id = str(id)
            a = id[len(id) // 2 :]
            b = id[0 : len(id) // 2]
            if a == b:
                invalids += int(id)
    print(f"Result Part1: {invalids}")


def part2(dataset):
    invalids = 0
    for item in dataset:
        item_list = list(range(item[0], item[1] + 1))
        # print("---",item[0], item[1])

        res = []
        for id in item_list:
            if re.match(r"^(.*)\1+$", str(id)):
                res.append(id)
                invalids += id
        # print(res)

    print(f"Result Part2: {invalids}")


def main():
    dataset = list(open("big.txt", "r").readlines()[0].split(","))
    dataset = [tuple(map(int, x.split("-"))) for x in dataset]

    part1(dataset)
    part2(dataset)


if __name__ == "__main__":
    main()
