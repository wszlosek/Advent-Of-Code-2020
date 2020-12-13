def commonCharacters(strings, n):
    MAX_CHAR = 26
    prim = [True] * MAX_CHAR
    l = 0

    for i in range(n):
        sec = [False] * MAX_CHAR

        for j in range(len(strings[i])):
            if (prim[ord(strings[i][j]) - ord('a')]):
                sec[ord(strings[i][j]) - ord('a')] = True

        for i in range(MAX_CHAR):
            prim[i] = sec[i]

    for i in range(26):
        if (prim[i]):
            l += 1

    return l


def part1(sentences):
    sum = 0

    for i in sentences:
        sum += len(i)

    return sum


def part2(lines):
    arr = []
    p2 = 0

    for l in lines:
        if l != "":
            arr.append(l)
        else:
            p2 += commonCharacters(arr, len(arr))
            arr.clear()

    return p2


def main():
    with open("input.txt") as f:
        lines = f.read().split('\n')

    sentence = ""
    sentences = []

    for l in lines:
        if l != "":
            sentence += l
        else:
            sentence = "".join(set(sentence))
            sentences.append(sentence)
            sentence = ""

    print(f"Part 1: {part1(sentences)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()