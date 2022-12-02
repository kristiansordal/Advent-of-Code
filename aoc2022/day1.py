def part1(elves):
    sums=[]
    for elf in elves:
        sums.append(sum(elf))
    m=sums[0]
    for s in sums:
        if s>m:
            m=s
    print(m)
        
    sums=sorted(sums, reverse=True)
    print(sums[0]+sums[1]+sums[2])



def main():
    with open('input/day1.in') as f:
        inp = [l.strip() for l in f.readlines()]
    
    elves = []
    elf = []
    for l in inp:
        if l != '':
            elf.append(int(l))
        else :
            elves.append(elf)
            elf = []

    part1(elves)

main()