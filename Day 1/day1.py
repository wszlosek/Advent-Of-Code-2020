def part1(lines):
    for a in lines:
        for b in lines:
            if (int(a) + int(b) == 2020):
                print(f"Part 1: {int(a) * int(b)}")
                return

def part2(lines):
    for a in lines:
        for b in lines:
            for c in lines:
                if(int(a) + int(b) + int(c) == 2020):
                    print(f"Part 2: {int(a) * int(b) * int(c)}")
                    return


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()