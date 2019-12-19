import math

inputfile = "input/input-day2.txt"
inputdata = []
mem = []

def ReadInput():
    file = open(inputfile,"r")
    for line in file:
        for part in line.split(","):
            inputdata.append(int(part))

    file.close

def IntProgramm():
    ic = 0
    while True:       
        optCode = mem[ic]
        posInp1 = mem[ic+1]
        posInp2 = mem[ic+2]
        posOut1 = mem[ic+3] 
        if optCode==99:           
            return mem[0]

        mem[posOut1] = ExecuteOptCode(optCode,mem[posInp1],mem[posInp2])
        ic += 4
        
    
def ExecuteOptCode(optCode,val1,val2):
    Operation = {
        1: val1 + val2,
        2: val1 * val2
    }
    
    return Operation.get(optCode, lambda: "Invalid Operation")

def Day2Example():
    global mem
    demodata = "1,9,10,3,2,3,11,0,99,30,40,50"
    for pos in demodata.split(","):
        mem.append(int(pos))

    print(IntProgramm())   
def Day2():
    global mem
    ReadInput()
    mem = [x for x in inputdata]
    mem[1] = 12
    mem[2] = 2

    print(IntProgramm())

def Day2PartB():
    global mem
    ReadInput()
    for noun in range(0,100):
        for verb in range(0,100):
            mem = [x for x in inputdata]
            mem[1] = noun
            mem[2] = verb
            if IntProgramm() == 19690720:
                print(noun*100+verb)


if __name__ == "__main__":
	print("Day 2")
	#ReadInput()
	Day2PartB()
   # IntProgramm()
	
