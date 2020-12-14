def part1(lines):
    acc = 0
    i = 0
    iS = []

    while True:
        instruction = lines[i][0:3]

        if i in iS:
            break
        else:
            iS.append(i)

        if lines[i][4] == "-":
            value = int(lines[i][4:])
        else:
            value = int(lines[i][5:])

        if instruction == "acc":
            acc += value
            i += 1

        elif instruction == "jmp":
            i += value

        else:
            i += 1

        if i >= len(lines):
            break

    return acc


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {part1(lines)}")


if __name__ == "__main__":
    main()