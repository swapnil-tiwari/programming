list=[1,5,1,0,6,0]
sums=[]
for x in range (0,len(list)):
    for y in range(0,len(list)):
        if(x!=y):
            sums.append(list[x]+list[y])
        
print(sums)
X=15
for x in range(0,len(sums)):
    key=X-sums[x]
    if(key in sums):
        print(1)
        break

    