n=int(input())
alldata=input()
data=[]
all=alldata.split()
for i in range(n):
    data.append(int(all[i]))
data.sort()
if n%2==1:
    h=int(n/2)
    print(data[h])
else:
    h=int(n/2)
    h=h-1
    print(data[h])

