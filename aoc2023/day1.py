import regex as re

data = open("input/1.in").read().splitlines()
p1, p2 = 0, 0
d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for l in data:
    nl = re.findall(rf"(\d|" + "|".join(d.keys()) + ")", l, overlapped=True)
    nums_p1 = list(map(int, filter(lambda x: not x.isalpha(), l)))
    nums_p2 = [int(x) if len(x) == 1 else d[x] for x in nl]
    p1 += nums_p1[0] * 10 + nums_p1[-1]
    p2 += nums_p2[0] * 10 + nums_p2[-1]

print(f"P1: {p1}, P2: {p2}")
