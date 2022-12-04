import re
def overlaps(ls):
    n = 0
    for l in ls:
        l1 = (range(l[0]), l[1]+1)
        l2 = (range(l[2]), l[3]+1)
        if all([True if x in l2 else False for x in l1]) == True or all([True if x in l1 else False for x in l2]) == True:
            n += 1
    return n

def main():
    with open('input/day4.in') as f:
        ls = [list(map(int, re.sub('\D', " ", l).split())) for l in f]
    print(overlaps(ls))
main()
