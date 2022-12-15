import re
xPos = set()
yLine = 2000000
with open("input/day15.in") as fp: 
    lines = fp.read().splitlines()  
    for line in lines[:]:
        row = re.sub("[^0-9=-]","", line)[1:].split('=')
        sx,sy,bx,by = row
        sx = int(sx); sy = int(sy); bx = int(bx); by = int(by)
        myBDist = abs(bx-sx)+abs(by-sy)
        myYDist = abs(yLine-sy)
        if myYDist <= myBDist:
            for i in range (sx-(myBDist-myYDist),sx+(myBDist-myYDist)):
                xPos.add(i)
print("Def not beacon Pos: ", len(xPos))