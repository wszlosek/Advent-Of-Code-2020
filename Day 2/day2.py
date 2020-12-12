def part1(s, a, b, char):
    z = s[3].count(char)

    if(z >= a and z <= b):
        return True
    return False


def part2(s, a, b, char):
    if((char == s[3][a] and char != s[3][b])
            or (char != s[3][a] and char == s[3][b])):
        return True
    return False


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    p1 = 0
    p2 = 0

    for l in lines:
        s = l.replace("-", " ").split(" ")

        char = s[2][0]
        a = int(s[0])
        b = int(s[1])

        if(part1(s, a, b, char)):
            p1 += 1
        if (part2(s, a-1, b-1, char)):
            p2 += 1

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()