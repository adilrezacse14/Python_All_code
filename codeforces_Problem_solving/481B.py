def remover(takestr):
    pos = takestr.find("xxx")
    newstr = takestr[:pos] + takestr[pos + 1:]
    return newstr
n=int(input())
mainstr=input()
item=1;
exst=mainstr.count("xxx")
if exst==0:
    print("0")
else:
    while 1:
        newstr2 = remover(mainstr)
        again = newstr2.count("xxx")
        mainstr = newstr2
        if again!=0:
            item=item+1
        else:
            break
    print(item)
