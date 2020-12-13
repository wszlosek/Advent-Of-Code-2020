import re

def shinyGold(g, graph):
    if g == "shiny gold":
        return True

    elif g != "":
        return any(shinyGold(next, graph) for i, next in graph[g])

    return False

def part1(graph):
    p1 = 0

    for g in graph.keys():
        if(shinyGold(g, graph)):
            p1 += 1

    return p1 - 1


def part2(g, graph):
    if g == "":
        return 1

    return sum(int(i) * part2(next, graph)
               for i, next in graph[g]) + 1


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    graph = {}
    for l in lines:
        regex = re.match('(.+?) bags', l)
        c1 = regex.group(1)
        c2 = re.findall('(\d+) (.+?) bag', l)

        if len(c2) > 0:
            graph[c1] = c2
        else:
            graph[c1] = [('0', '')]


    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2('shiny gold', graph) - 1}")


if __name__ == "__main__":
    main()