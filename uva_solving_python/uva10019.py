case=int(input())
for i in range(case):
    now=input()
    dec=int(now)
    binaryformat=bin(dec)[2:]
    strformate=str(binaryformat)
    b1=strformate.count("1")
    hexformat=int(now,16)
    binaryformat=bin(hexformat)[2:]
    binaryformat=str(binaryformat)
    b2=binaryformat.count("1")
    print("%d %d"%(b1,b2))