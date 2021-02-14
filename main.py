from sys import argv #sad, i wanna try and make this using only the STD lib, but i need this for argv. darn you python
def throw(exception):
    print(str(exception))
    exit()
addr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
vaddr = [0,0,0,0,0,0,0,0]
var = {} #todo: make this impact available address space?
with open(argv[1]) as file:
    lines = [line.rstrip('\n').split(' ') for line in file]
#print(lines)
i=0
while i < len(lines):
    inst = lines[i]
    if inst[0] == 'put':
        #check and make sure that args are within constraints
        if int(inst[1]) > 1 or int(inst[1]) < 0:
            throw('Attempted to put value other than 0 or 1 in address space')
        if int(inst[2]) > len(addr) - 1:
            throw('Attempted to write value to address index higher than available')
        #if not, actually do code
        addr[int(inst[2])] = int(inst[1])
    if inst[0] == 'vput':
        #check and make sure that args are within constraints
        if int(inst[1]) > 1 or int(inst[1]) < 0:
            throw('Attempted to put value other than 0 or 1 in address space')
        if int(inst[2]) > len(vaddr) - 1:
            throw('Attempted to write value to address index higher than available')
        #if not, actually do code
        vaddr[int(inst[2])] = int(inst[1])
    if inst[0] == 'prnt':
        newvaddr = [str(i) for i in vaddr]
        print(chr(int(''.join(newvaddr[:-1]), 2)), end='')
        if vaddr[len(vaddr) - 1] == 1:
            print('')
    if inst[0] == 'equl':
        if addr[int(inst[1])] == addr[int(inst[2])]:
            addr[int(inst[3])] = 1
        else:
            addr[int(inst[3])] = 0
    if inst[0] == 'vequl':
        if vaddr[int(inst[1])] == vaddr[int(inst[2])]:
            vaddr[int(inst[3])] = 1
        else:
            vaddr[int(inst[3])] = 0
    if inst[0] == 'cpy':
        vaddr[int(inst[2])] = addr[int(inst[1])]
    if inst[0] == 'flsh':
        addr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if inst[0] == 'vflsh':
        vaddr = [0,0,0,0,0,0,0,0]
    if inst[0] == 'mov':
        vaddr[int(inst[2])] = addr[int(inst[1])]
        vaddr[int(inst[1])] = 0
    if inst[0] == 'dump':
        print(addr)
    if inst[0] == 'vdump':
        print(vaddr)
    if inst[0].startswith('#'):
        pass #comments
    if inst[0] != 'jmp':
        i+=1
    if inst[0] == 'jmp':
        i = int(inst[1])
