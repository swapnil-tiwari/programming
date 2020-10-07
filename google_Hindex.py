def hindex(arr,n,size):
    # print(n,size)
    count=0
    for i in range(0,size):
        if(arr[i]>=n):
            count+=1
    
    if(count>=n):
        return n
    else:
        return hindex(arr,n-1,size)

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    hindexs=[]
    size=n
    while(size):
        hindexs.append(hindex(arr,n,size))
        size=size-1
        n=n-1
    # hindexs.append(hindex(arr,n,size))
    # # hindexs.append(hindex(arr,n-1,size-1))
    hindexs.sort()
    hindexs=list(map(str,hindexs))
    hindexs=" ".join(hindexs)
    return hindexs
    

t=int(input())
for i in range(0,t):
    
    ans=main()
    res='Case #{caseno}: {ans}'.format(caseno=i+1,ans=ans)
    print(res)
    