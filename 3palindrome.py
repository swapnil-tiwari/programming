
def isPalin(string):
    return (len(string)>=2 and string==string[::-1])
def main():
    string=input()
    p1=''
    p2=''
    p3=''
    x=0
    i=0
    count=0
    for x in range(i,len(string)+1):

        subs=string[0:x]
        # print(subs)
        if(isPalin(subs)):
            i=x
            count+=1
            p1=subs
            break
        
    
    for x in range(i,len(string)+1):
        subs=string[i:x]
        # print(subs)
        if(isPalin(subs)):
            i=x
            count+=1
            p2=subs
            break
    
    for x in range(i,len(string)+1):
        subs=string[i:x]
        if(isPalin(subs)):
            i=x
            count+=1
            p3=subs
            break
    
    # print(p1,p2,p3)
    if(count==3 and i==len(string)):
        print(p1)
        print(p2)
        print(p3)
    else:
        print('Impossible')
    
main()   
# print(isPalin('nawsyan'))