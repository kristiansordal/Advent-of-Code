import re
with open('input/day4.in') as f:
    nums = [list(map(int, re.sub('\D+', " " ,l.strip()).split(' '))) for l in f]
contains = len(list(filter (lambda x: x == True, (list(map(lambda x: (x[0] <= x[2] and x[1] >= x[3]), nums))))))
print(contains)
