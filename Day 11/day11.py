from copy import deepcopy
from itertools import chain

def adj(adjrows, i):
    return list(chain(*[[ x[i] for i in range(i-1, i+2) ] for x in adjrows ]))


def part1(lines):
    l1 = deepcopy(lines)
    d = 0
    rows = [None, ['.' for x in range(len(lines[0]))] + ['.'], lines[0] + ['.']]

    for j in range(len(lines)):
        rows.pop(0)
        rows.append(lines[j+1] + ['.']) \
            if j+1 in range(len(lines)) \
            else rows.append(['.' for i in range(len(lines[0]))] + ['.'])

        for i in range(len(lines[0])):
            cell = lines[j][i]

            if cell == "#":
                adjm = adj(rows, i).count('#') - 1
                if adjm > 3:
                    l1[j][i] = 'L'
                    d += 1

            elif cell == "L":
                adjm = adj(rows, i).count('#')
                if adjm == 0:
                    l1[j][i] = '#'
                    d += 1

    if d > 0:
        return part1(l1)

    return lines


def main():
    with open("input.txt") as f:
        lines = [list(x) for x in f.read().replace('L', '#').splitlines()]

    count = []
    [count.append(x.count('#')) for x in part1(lines)]
    p1 = sum(count)

    print(f"Part 1: {p1}")


if __name__ == "__main__":
    main()