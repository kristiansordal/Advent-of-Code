import re
def part1(y1):
    vy = (abs(y1) - 1)
    maxHeight = (vy*(vy+1))/2
    print(round(maxHeight))

def part2(x1,x2,y1,y2):

    def hitsTarget(vx,vy):
        x = y = 0
        while True:
            if x > x2: return False
            if vx == 0 and not x1 <= x <= x2: return False
            if vx == 0 and y < y1: return False

            if x1 <= x <= x2 and y1 <= y <=y2: return True

            x += vx
            y += vy

            if vx > 0:
                vx -= 1

            vy -= 1

    yMax = max(abs(y1), abs(y2))
    velocity = 0

    for vx in range(x2 + 1):
        for vy in range(-yMax, yMax +1):
            velocity += hitsTarget(vx,vy)
            
    print(velocity) 
# def part2(xf_min, xf_max, yf_min, yf_max):
    
#     def hits_target(vx, vy):
#         x = y = 0
#         while True:
#             # breaking conditions
#             if x > xf_max: return False
#             if vx == 0 and not xf_min <= x <= xf_max: return False
#             if vx == 0 and y < yf_min: return False
            
#             # target condition
#             if xf_min <= x <= xf_max and yf_min <= y <= yf_max: return True
            
#             x += vx
#             y += vy
            
#             if vx > 0: vx -= 1
#             vy -= 1
    
#     y_max = max(abs(yf_min), abs(yf_max))
#     distinct_velocitys = 0
    
#     for vx in range(xf_max + 1):
#         for vy in range(-y_max, y_max + 1):
#             distinct_velocitys += hits_target(vx, vy)
            
#     print(distinct_velocitys)
def main():
    with open('C:\dev\Advent of Code\Advent of Code 2021\Day 17\inputDay17.txt') as file:
        line = file.read().strip()
        input = re.split('[=|..|,]', line) 
        x1 = int(input[1])
        x2 = int(input[3])
        y1 = int(input[5])
        y2 = int(input[7])


    part1(y1)
    part2(x1,x2,y1,y2)

if __name__ == '__main__':
    main()