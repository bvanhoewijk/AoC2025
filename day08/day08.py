import math
from itertools import combinations
from pprint import pprint


def part1(dataset):
    distances = {}
    for box_a, box_b in list(combinations(dataset, 2)):
        distances[(box_a, box_b)] = math.dist(box_a, box_b)

    # Sort on distance
    distances = sorted(distances.items(), key=lambda x: x[1])

    # Prepare circuit where every node is seperate:
    circuit = [set([x]) for x in dataset]

    # Loop 1000 times (for big dataset. For small fill in 10:)
    for d in distances[:1000]:
        node1, node2 = d[0][0], d[0][1]

        values1 = find(node1, circuit)
        values2 = find(node2, circuit)

        # Remove old:
        circuit = [x for x in circuit if x not in [values1, values2]]

        # Add new
        circuit.append(values2 | values1)

    circuit = sorted(circuit, key=lambda x: len(x), reverse=True)
    # Biggest three nodes:
    res = 1
    for i in range(3):
        res *= len(circuit[i])
    print("Solution part 1:", res)


def part2(dataset):
    distances = {}
    for box_a, box_b in list(combinations(dataset, 2)):
        distances[(box_a, box_b)] = math.dist(box_a, box_b)

    # Sort on distance
    distances = sorted(distances.items(), key=lambda x: x[1])

    # Prepare circuit where every node is seperate:
    circuit = [set([x]) for x in dataset]

    # Loop through all distances until done:
    for d in distances:
        node1, node2 = d[0][0], d[0][1]

        values1 = find(node1, circuit)
        values2 = find(node2, circuit)

        # Remove old:
        circuit = [x for x in circuit if x not in [values1, values2]]

        # Add new
        circuit.append(values2 | values1)
        if len(circuit) == 1:
            print(
                f"Solution part 2: {node1[0] * node2[0]} ({i+1}/{len(distances)} merges)"
            )
            break


def find(x, circuit):
    for item in circuit:
        if x in item:
            return item
    return None


if __name__ == "__main__":
    dataset = [
        tuple(map(int, item.strip().split(",")))
        for item in open("big.txt", "r").readlines()
    ]

    part1(dataset)
    part2(dataset)
