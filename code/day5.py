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
        param1 = 0
        param2 = 0
        if opcode==3:
            out = mem[ic+1]
        elif opcode == 4:
            out = 0
            param = 1
            param1 = GetParameterValue(param,modes,mem[ic+param]) 
        else:
            param = 1
            param1 = GetParameterValue(param,modes,mem[ic+param]) 
            param = 2
            param2 = GetParameterValue(param,modes,mem[ic+param])
            param = 3
            out = mem[ic+param]

        result = ExecuteOptCode(opcode,ic,inputvalue,param1,param2) 
        
        if out > 0:
            mem[out] = result

        ic += GetNextOperation(opcode)

def GetParameterValue(param,modes,memval):
    return mem[memval] if not modes[param-1] else memval

def ExecuteOptCode(opCode,mempos,inputvalue,val1,val2):
    global mem
    if opCode == 1:
        return val1 + val2
    elif opCode == 2:
        return val1 * val2
    elif opCode == 3:
        return inputvalue
    elif opCode == 4:
        print(val1)

def GetNextOperation(opcode):
    Jump = {
        1: 4,
        2: 4,
        3: 2,
        4: 2
    }
    return Jump.get(opcode)

if __name__ == "__main__":
    ReadInput()
    CopyToMem()
    IntProgramm(1)

