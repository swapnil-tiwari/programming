l=['548', '546', '60', '54']
l=[11,9,99,22,252,965]
l.sort(reverse=True)
l=list(map(str,l))
lens=[1,2,3]
all=[]
print(l)
for x in range(1,len(l[0])+1):
    sublen=[]
    for each in l:
        if(len(each)==x):
            sublen.append(each)
    all=all+sublen

print(all)
