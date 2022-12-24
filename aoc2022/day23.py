import numpy as np
def part1(grid):

    r = 0
    rounds = 10
    N = [(0,-1), (-1,-1),(1,-1)]
    S = [(0,1), (-1,1),(1,1)]
    W = [(-1,0), (-1,-1),(-1,1)]
    E = [(1,0), (1,-1),(1,1)]

    north = (0,-1)
    south = (0,1)
    west = (-1, 0)
    east = (1,0)
    while r < rounds:

        #propose moves
        proposed = {}
        for pos in grid:
            if check_pos(grid, pos, N):
                if not (pos[0] - 1, pos[1]) in proposed.values():
                    proposed[pos] = (pos[0] + north[0], pos[1] + north[1])
                else:
                    proposed = {key:val for key, val in proposed.items() if val != pos}
            elif check_pos(grid, pos, S):
                if not (pos[0] + 1, pos[1]) in proposed.values():
                    proposed[pos] = ((pos[0] + south[0], pos[1] + south[1]))
                else:
                    proposed = {key:val for key, val in proposed.items() if val != pos}
            elif check_pos(grid, pos, W):
                if not (pos[0], pos[1] - 1) in proposed.values():
                    proposed[pos] = ((pos[0] + west[0], pos[1] + west[1]))
                else:
                    proposed = {key:val for key, val in proposed.items() if val != pos}
            elif check_pos(grid, pos, E):
                if not (pos[0], pos[1] + 1) in proposed.values():
                    proposed[pos] = ((pos[0] + east[0], pos[1] + east[1]))
                else:
                    proposed = {key:val for key, val in proposed.items() if val != pos}
        
        # move elves
        for key in proposed:
            if proposed[key] in grid and :
                grid.remove(key)
                grid.add(proposed[key])

        N = S
        S = W
        W = E
        E = N

        north = south
        south = west
        west = east
        east = north
        r += 1
            
    
        xPos = []
        yPos = []
        for x in grid:
            xPos.append(x[1])
            yPos.append(x[0])

        xMax = max(xPos)
        yMax = max(yPos)

        ls = []
        for y in range(yMax + 5):
            line = ""
            for x in range(xMax + 5):
                if (y,x) in grid:
                    line += '#'
                else:
                    line += '.'
            print(line)

        print('\n')
    # print(np.matrix(ls))


    return (xMax * yMax)  - len(grid)

def check_pos(grid, pos,  dir):
    check = []
    for d in dir:
        check.append((pos[0] + d[0], pos[1] + d[1]))
    return not any(check) in grid
                        
                    


def main():
    with open('input/day23.in') as f:
        grid = []
        for i, l in enumerate(f.readlines()):
            for j, r in enumerate(l):
                if r == '#':
                    grid.append((i,j))


    print(part1(set(grid)))

if __name__ == '__main__':
    main()