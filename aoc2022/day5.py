import re


def part1(stack, moves):
    for move in moves:
        for _ in range(move[0]):
            f = move[1] - 1
            t = move[2] - 1
            if len(stack[f][1]) != 0:
                el = stack[f][1].pop(0)
                stack[t][1].insert(0, el)

    msg = ''
    for x in stack:
        msg += x[1][0]
    print(msg)


def part2(stack, moves):
    for move in moves:
        f = move[1] - 1
        t = move[2] - 1
        m = move[0]

        els = stack[f][1][:m]
        for e in reversed(els):
            stack[t][1].insert(0, e)
            stack[f][1].pop(0)

    msg = ''
    for x in stack:
        msg += x[1][0]

    print(msg)


def main():
    stack = [(1, []), (2, []), (3, []), (4, []), (5, []),
             (6, []), (7, []), (8, []), (9, [])]
    moves = []

    with open('input/day5.in') as f:
        n = False
        for l in f.readlines():

            if not n:
                for i, char in enumerate(l):
                    if char.isupper():
                        stack[int((i+1)/3)][1].append(char)
            else:
                ls = list(map(int, re.sub('\D', " ", l).split()))
                moves.append(ls)

            if 'okay' in l:
                n = True

    stackCopy = stack
    moveCopy = moves
    part1(stack, moves)
    part2(stackCopy, moveCopy)


if __name__ == '__main__':
    main()
