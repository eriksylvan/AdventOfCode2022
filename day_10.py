# day 10

# https://adventofcode.com/2022/day/10



inputFile='input/10_input'
#inputFile='input/10_test_input'
#inputFile='input/10_test2'

class Instruction:
    # A directory have one parent directory and can have directories and files
    def __init__(self, ins, val):
        self.instr = ins
        self.val = val

instructions=[]
with open(inputFile) as input:
    
    for row in input:
        ins=''
        val=None
        # print(row)
        i = row.strip().split(' ')
        ins = i[0]
        if ins != "noop":
            val = int(i[1])
    
        #print (ins, val)
        instructions.append(Instruction(ins,val))


xMem = 1
pRam = [Instruction('noop',None)]
i = 0
step = 1
ans = 0
run = True
spritePos = 1
CRT = []
while run:
    # Add next instruction
    if i<len(instructions):
        if instructions[i].instr == 'noop': 
            #dc = 1
            pRam.append(instructions[i])
        if instructions[i].instr == 'addx': 
            #dc = 2
            pRam.append(Instruction('noop',None))
            pRam.append(instructions[i])
    # Execute
    
    if pRam[0].instr=='addx':
        xMem = xMem + pRam[0].val
        #print('step:',step,'->',pRam[0].val, xMem)
    pRam.pop(0)
    if step in(20,60,100,140,180,220):
        #print('step:',i, xMem,i*xMem)
        ans += (step * xMem)
        #print('------------------')
    #print('step:',step, xMem,step*xMem)
    # End of program
    if len(pRam) == 0: run = False 
    i+=1
    
    spritePos = xMem 
    if ((step % 40)) in(spritePos, spritePos+1, spritePos+2):
        CRT.append('#')
    else:
        CRT.append('.')
   
    
    step+=1
    
    


print("Day10 part1:",ans)
print()
print()
    
#print(CRT)

print("Day10 part2:")
for x in range(len(CRT)):
    if(x%40)==0:
        print('')
    print(CRT[x],end='')
    





