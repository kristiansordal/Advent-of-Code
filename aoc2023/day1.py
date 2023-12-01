import regex as re

with open("input/1.in") as f:
    data = f.read().splitlines()
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
        nums = list(map(int, filter(lambda x: not x.isalpha(), l)))
        p1 += nums[0] * 10 + nums[-1]
        p = "|".join(d.keys())
        nl = re.findall(rf"(\d|{p})", l, overlapped=True)
        nums = [int(x) if len(x) == 1 else d[x] for x in nl]
        p2 += nums[0] * 10 + nums[-1]

    print(p1)
    print(p2)
