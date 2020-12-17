def part1(lines):
    for a in lines:
        for b in lines:
            if (int(a) + int(b) == 2020):
                return (int(a) * int(b))


def part2(lines):
    for a in lines:
        for b in lines:
            for c in lines:
                if(int(a) + int(b) + int(c) == 2020):
                    return (int(a) * int(b) * int(c))


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()


    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()