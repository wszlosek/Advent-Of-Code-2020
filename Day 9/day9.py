def part1(lines):
    for i in range(26, len(lines)):
        hLines = lines[i-25:i]
        sums = []

        for l1 in range(25):
            for l2 in range(25):
                if l1 != l2:
                    sums.append(int(hLines[l1])+int(hLines[l2]))

        if (int(lines[i]) not in sums):
            return lines[i]

        sums.clear()


def part2(lines):
    x = int(part1(lines))
    n = len(lines)
    res = int(lines[0])
    start = 0

    for i in range(1, n+1):

        while(res > x and start < i-1):
            res -= int(lines[start])
            start += 1

        if res == x:
            break

        if i < n:
            res += int(lines[i])

    arr = [int(lines[l]) for l in range(start, i)]

    return (min(arr) + max(arr))


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}", end="")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()