import math

inputdata = []
inputfile = "input/input-day3.txt"
grid = []
# for real
gridsizex = 17000
gridsizey = 13000
startx = 7200 # int(gridsize / 2)
starty = 9000 # int(gridsize / 2)
testing = False



def SetTestData1():
	testing = True
	inputdata.clear()
	inputdata.append("R75,D30,R83,U83,L12,D49,R71,U7,L72")
	inputdata.append("U62,R66,U55,R34,D71,R55,D58,R83")
	# answer = 159

def SetTestData2():
	testing = True
	inputdata.clear()
	inputdata.append("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
	inputdata.append("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
	# answer = 135

def ManhattanDistance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

def LayWire(wire,val):
    posx = startx
    posy = starty
    for part in wire.split(","):
        posx,posy = LayWireDirection(part[0],int(part[1::]),posx,posy,val)

def MoveDirection(direction,posx,posy):
    if direction == "R":
        posx += 1
    elif direction == "L":
        posx -= 1
    elif direction == "U":
        posy += 1
    elif direction == "D":
        posy -= 1

    return posx,posy

def LayWireDirection(direction,distance,posx,posy,val):
    for i in range(0,distance):        
        posx,posy = MoveDirection(direction,posx,posy)
        if (posy < 0) or (posx < 0):
	        print("Grid too small: %d,%d" %  (posx, posy))      
        grid[posx][posy] |= val      
   
    return posx,posy

def ReadInput():
    file = open(inputfile,"r")
    for line in file:
        inputdata.append(line)

def InitGrid():
    grid.clear()
    for x in range (0,gridsizex):
        grid.append([0 for y in range(0,gridsizey)])

def Day3():
   
    LayWire(inputdata[0],1)
    LayWire(inputdata[1],2)
    closest = 0

    for x in range(0,gridsizex):
        for y in range(0,gridsizey):
            if grid[x][y] == 3:
                distance = ManhattanDistance(startx, starty, x, y)
                if closest == 0 or distance < closest:
                    closest = distance
                
    print(closest)
if __name__ == "__main__":
    ReadInput()
    #SetTestData2()
    InitGrid()
    print(gridsizex)
    Day3()
