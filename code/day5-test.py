import math

inputfile = "input-day5-krisje.txt"
inputfile = "input-day5.txt"
inputdata = []
mem = []

def ReadInput():
    file = open(inputfile,"r")
    for line in file:
        for part in line.split(","):
            inputdata.append(int(part))

    file.close

def IntProgramm(inputvalue):
    ic = 0
    while True:     
        instruction = mem[ic]
        if instruction == 99:           
            return mem[0]

        opcode = instruction % 100
        instruction = (instruction - opcode) / 100
        mode1 = instruction % 10
        instruction = (instruction - mode1) / 10
        mode2 = instruction % 10
        instruction = (instruction - mode2) / 10
        mode3 = instruction % 10

        optCode = opcode
        instruction -= optCode        
        posInp1 = mem[ic+1]        
        posInp2 = mem[ic+2]        
        posOut1 = mem[ic+3] 
        if optCode == 3:
            posOut1 = posInp1
            posInp1 = inputvalue     
            mode1 = False       
            ic -= 2       

        if mode1 == 0:
            posInp1 = mem[posInp1]
        
        if mode2 == 0:
            posInp2 = mem[posInp2]

        if optCode == 4:
            print("Value = %d",posInp1)
            ic -= 2       
        else:
            mem[posOut1] = ExecuteOptCode(optCode,posInp1,posInp2)
        
        ic += 4

def TestIntProgramm():
    global mem
    params = "1002,4,3,4,33"   
    mem = [int(x) for x in params.split(",")]   
    print(mem)
    IntProgramm(5)
    print(mem[4])

def Day5Part1(inputvalue):
    global mem       
    mem = [x for x in inputdata] 
    IntProgramm(inputvalue)
    
def ExecuteOptCode(optCode,val1,val2):
    Operation = {
        1: val1 + val2,
        2: val1 * val2,
        3: val1
    }
    
    return Operation.get(optCode, lambda: "Invalid Operation")

if __name__ == "__main__":
    ReadInput()
    Day5Part1(1)
