def main():
    lst=input()
    lst=list(map(int,lst.split()))
    flag=False
    for x in range(0,len(lst)+1):
        flag=False

        for y in range(0,x):
            if(lst[x]<=lst[y]):
                flag=True
                break
        for y in range(x+1,len(lst)):
            if(lst[x]>=lst[y]):
                flag=True
                break
        if(not(flag)):
            print(lst[x])
    

main()

def maxIndexDiff(self,arr,n):
	    max=0
		for i in range(0,n+1):
		    j=n-1
		    while(arr[j]>arr[i]):
		        j-=1
		        
		    if(j-i>max):
		        max=j-i
	    return max