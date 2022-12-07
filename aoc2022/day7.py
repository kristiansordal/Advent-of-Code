def sizes(dirs):
    stack = []
    sizes = []
                                
    for d in dirs:
        if d[0] == 'cd':
            if d[1] == '..':
                sizes.append(stack.pop(-1))
                if stack:
                    stack[-1] += sizes[-1]
            else:
                stack.append(0)
        elif d == 'ls':
            continue
        elif d[0] == 'dir':
            continue
        else:
            stack[-1] += int(d[0])

    while stack:
        sizes.append(stack.pop(-1))
        if stack:
            stack[-1] += sizes[-1]

    x = 0
    for n in sizes:
        if n < 100000:
            x += n

    biggest = max(sizes) 
    o = []
    for n in sizes:
        if biggest - 40000000 <= n:
            o.append(n)

    print(o)
    return x, min(o)
   
def main():
    with open('input/day7.in') as f:
        dirs = [ (line.strip().split(' ')[0], line.strip().split(' ')[1])if line != 'ls\n' else line.strip() for line in f.readlines()]
    print(sizes(dirs))

main()