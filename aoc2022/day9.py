def part1(moves):
    h = [0,0]
    t = [0,0]
    curr = ''
    visited = set()
    start = False

    for x, m in enumerate(moves):
        prev = curr
        curr = m[0]


        if m[0] == 'L':
            for i in range(m[1]):
                h[1] -= 1
                if start:
                    if prev == 'R' and i > 3:
                        t[1] -= 1
                    elif prev != 'R':
                        t[1] -= 1
                start = True
                visited.add((t[0], t[1]))

        elif m[0] == 'R':
            for i in range(m[1]):
                h[1] += 1
                if start:
                    if prev == 'L' and i > 3:
                        t[1] += 1
                    elif prev != 'L':
                        t[1] += 1
                start = True
                visited.add((t[0], t[1]))
        elif m[0] == 'U':
            for i in range(m[1]):
                if prev == 'L' and i == 1:
                    h[0] += 1
                    h[1] -= 1
                elif prev == 'R' and i == 1:
                    h[0] += 1
                    h[1] += 1
                else:
                    h[0] += 1
                if start:
                    if prev == 'D' and i > 3:
                        t[0] += 1
                    elif prev == 'L' and i == 1:
                        t[0] += 1
                        t[1] -= 1
                    elif prev == 'R' and i == 1:
                        t[0] += 1
                        t[1] += 1
                    elif prev != 'D':
                        t[0] += 1
                visited.add((t[0], t[1]))
        elif m[0] == 'D':
            for i in range(m[1]):
                if prev == 'L' and i == 1:
                    h[0] -= 1
                    h[1] -= 1
                elif prev == 'R' and i == 1:
                    h[0] -= 1
                    h[1] += 1
                else:
                    h[0] -= 1
                if start:
                    if prev == 'U' and i > 3:
                        t[0] -= 1
                    elif prev == 'L' and i == 1:
                        t[0] -= 1
                        t[1] -= 1
                    elif prev == 'R' and i == 1:
                        t[0] -= 1
                        t[1] += 1
                    elif prev != 'U':
                        t[0] -= 1
                    
                visited.add((t[0], t[1]))
    print(len(visited))

def main():
    with open('input/day9.in') as f:
        moves = [(line.strip().split(' ')[0], int(line.strip().split(' ')[1])) for line in f.readlines()]
    
    print(moves)
    part1(moves)


if __name__ == '__main__':
    main()