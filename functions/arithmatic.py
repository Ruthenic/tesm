def addition(addr,vaddr,inst):
    val = int(str(bin(int(inst[1])+int(inst[2]))).replace("0b", ""))
    for i in range(0,len(str(val))):
        addr[len(addr)-i] = str(val)[len(str(val))-i]
    return addr,vaddr
