def part1(lines, lhX, lhY, right, down):
    x = 0
    y = 0
    tree = 0

    while y < lhY-1:
        x += right
        y += down

        if(x >= lhX):
            x -= lhX

        if(lines[y][x] == "#"):
            tree += 1

    return tree


def part2(lines, lhX, lhY):
    x1 = part1(lines, lhX, lhY, 1, 1)
    x2 = part1(lines, lhX, lhY, 3, 1)
    x3 = part1(lines, lhX, lhY, 5, 1)
    x4 = part1(lines, lhX, lhY, 7, 1)
    x5 = part1(lines, lhX, lhY, 1, 2)

    return x1 * x2 * x3 * x4 * x5


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    lhX = len(str(lines[0]))
    lhY = len(lines)

    p1 = part1(lines, lhX, lhY, 3, 1)
    p2 = part2(lines, lhX, lhY)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()