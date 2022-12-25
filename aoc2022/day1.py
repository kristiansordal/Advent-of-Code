with open('input/day1.in') as f:
    inp = [[int(x) for x in l.split('\n') if x != ''] for l in f.read().split('\n\n')]
    ansP1 = max(map(sum, inp))
    ansP2 = sum(sorted(map(sum, inp), reverse = True)[:3])
print(f'Part 1: {ansP1}')
print(f'Part 2: {ansP2}')