def req(sentence, data):
    p = 0

    for d in data:
        if(sentence.count(d)):
            p += 1

    if(p == len(data)):
        return True
    return False


def findInArr(array, temp):
    for i in range(len(array)):
        if(array[i].find(temp) != -1):
            return i


def hcl(sentence):
    ch = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
          '9', 'a', 'b', 'c', 'd', 'e', 'f']

    for i in sentence:
        if(not(i in ch)):
            return False
    return True


def ecl(sentence):
    ch = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if(len(sentence) == 3 and sentence in ch):
        return True
    return False


def part1(lines, data):
    p1 = 0

    for l in lines:
        if(req(l, data)):
            p1 += 1

    return p1


def part2(lines, data):

    p2 = 0
    for l in lines:
        o = 0
        l = l.replace('\n', ' ')

        if(req(l, data)):
            sp = l.split()
            data2 = [findInArr(sp, data[0]), findInArr(sp, data[1]),
                     findInArr(sp, data[2]), findInArr(sp, data[3]),
                     findInArr(sp, data[4]), findInArr(sp, data[5]),
                     findInArr(sp, data[6])]

            if(1920 <= int(sp[data2[0]][4:]) <= 2002):
                o += 1

            if(2010 <= int(sp[data2[1]][4:]) <= 2020):
                o += 1

            if (2020 <= int(sp[data2[2]][4:]) <= 2030):
                o += 1

            if(sp[data2[3]][-2:] == "cm" and 150 <= int(sp[data2[3]][4:-2]) <= 193):
                o += 1
            if (sp[data2[3]][-2:] == "in" and 59 <= int(sp[data2[3]][4:-2]) <= 76):
                o += 1

            if(sp[data2[4]][4] == "#" and hcl(sp[data2[4]][5:])):
                o += 1

            if(ecl(sp[data2[5]][4:])):
                o += 1

            if (len(sp[data2[6]]) == 13):
                o += 1


            if(o == 7):
                p2 += 1

    return p2


def main():
    with open("input.txt") as f:
        lines = f.read().split('\n\n')

    data = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    print(f"Part 1: {part1(lines, data)}")
    print(f"Part 2: {part2(lines, data)}")


if __name__ == "__main__":
    main()