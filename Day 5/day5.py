def bin(line, length, left, right, par1, par2):
    low = 0
    high = length
    i = 0

    while i < len(line):
        mid = (high + low) // 2

        if line[i] == left:
            high = mid - 1

        elif line[i] == right:
            low = mid + 1

        elif (line[i] != par1 and line[i] != par2):
            break

        i += 1

    return mid + 1

def part1(lines):
    id = 0

    for l in lines:
        row = bin(l, 127, 'F', 'B', 'L', 'R')
        column = bin(l, 7, 'L', 'R', 'F', 'B')
        if(row * 8 + column > id):
            id = row * 8 + column

    return id


def part2(lines):
    data = []
    out = []

    for l in lines:
        row = bin(l, 127, 'F', 'B', 'L', 'R')
        column = bin(l, 7, 'L', 'R', 'F', 'B')
        id = 8 * row + column
        data.append(id)

    allSeat = set(range(min(data), max(data)))

    for i in allSeat:
        if not(i in data):
            out.append(i)

    for i in range(0, len(out)-1):
        if(out[i] + 8 != out[i+1]):
            return out[i+1]


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

if __name__ == "__main__":
    main()