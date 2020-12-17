def part1(lines):
    o1 = 1
    o3 = 0

    for l in lines:

        if (l == lines[-1]):
            o3 += 1
            break

        if (l+1 in lines):
            o1 += 1

        elif (l+3 in lines):
            o3 += 1

    return (o1 * o3)


def part2(lines):
    lines.append(lines[-1]+3)
    sof = {0:1}

    for l in lines:
        sof[l] = sof.get(l-3, 0) \
                 + sof.get(l-2, 0) \
                 + sof.get(l-1, 0)


    return sof[lines[-1]]


def main():
    with open("input.txt") as f:
        lines = f.read().split('\n')

    for l in range(len(lines)):
        lines[l] = int(lines[l])

    lines = sorted(lines)

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()