from intcode.IntCode import IntCode

D = [int(x) for x in open("input/2.in").read().split(",")]
ic = IntCode(D)
p1 = ic.execute(1, 12)

noun = 0
verb = 0
p2 = 0

while p2 != 19690720:
    for n in range(0, len(D)):
        for v in range(0, len(D)):
            ic = IntCode(D)
            noun, verb = n, v
            p2 = ic.execute(n, v)

p2 = 100 * noun + verb
print(p1)
print(p2)
