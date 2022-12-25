import itertools
alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open('input/day3.in') as f:
    print(sum(map(lambda x: alphabet.index(x), list(itertools.chain(*map(list, (map(lambda x: x[0].intersection(x[1]), (map(lambda x: (set(x[0]), set(x[1])), [(l.strip()[len(l.strip())//2:], l.strip()[:len(l.strip())//2]) for l in f.readlines()]))))))))))
