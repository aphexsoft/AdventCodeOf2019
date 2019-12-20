import math

inputfile = "input-day5-krisje.txt"
inputfile = "input/input-day5.txt"
inputdata = []
mem = []

def ReadInput():
    file = open(inputfile,"r")
    for line in file:
        for part in line.split(","):
            inputdata.append(int(part))

    file.close

def CopyToMem():
    global mem
    mem = [int(x) for x in inputdata]

def Test():
    global mem
    for op in "1002,4,3,4,33".split(","):
        inputdata.append(int(op))
    mem = [int(x) for x in inputdata]   
    IntProgramm(1)

def IntProgramm(inputvalue):
    ic = 0
    while True:        
        operation = mem[ic]
        max = round(operation,-3)
        opcode = (operation - max) % 100
        if opcode == 99:
            return 

        max *=10
        operation -= opcode
        step = 100
        modes = [] #false = position, true = immediate 
        while step < 1000000:
            step *= 10
            rest = (operation+step)%step!=0 
            if rest:
                operation -= step/10
            modes.append(rest)
        
        ic = ExecuteOptCode(opcode,ic,modes,inputvalue) 
        

def GetParameterValue(param,modes,memval):
    return mem[memval] if not modes[param-1] else memval

def ExecuteOptCode(opcode,mempos,modes,inputvalue):

    global mem
    val1 = GetParameterValue(1,modes,mem[mempos+1]) 
    
    if opcode == 1:       
        val2 = GetParameterValue(2,modes,mem[mempos+2]) 
        out = mem[mempos+3] 
        mem[out] = val1 + val2
    elif opcode == 2:        
        val2 = GetParameterValue(2,modes,mem[mempos+2]) 
        out = mem[mempos+3] 
        mem[out] = val1 * val2
    elif opcode == 3:
        val1 = mem[mempos+1]
        mem[val1] = inputvalue
    elif opcode == 4:        
        print(val1)
    elif opcode == 5:
        val2 = GetParameterValue(2,modes,mem[mempos+2])
        if val1 != 0:
            return val2        
    elif opcode == 6:
        val2 = GetParameterValue(2,modes,mem[mempos+2])
        if val1 == 0:
            return val2       
    elif opcode == 7:
        val2 = GetParameterValue(2,modes,mem[mempos+2])
        val3 = mem[mempos + 3]
        mem[val3] = 1 if val1 < val2 else 0
    elif opcode == 8:
        val2 = GetParameterValue(2,modes,mem[mempos+2])
        val3 = mem[mempos + 3]
        mem[val3] = 1 if val1 == val2 else 0 

    mempos += GetNextOperation(opcode)
    return mempos

def GetNextOperation(opcode):
    Jump = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4
    }
    return Jump.get(opcode)

if __name__ == "__main__":
    ReadInput()
    CopyToMem()
    IntProgramm(5)

