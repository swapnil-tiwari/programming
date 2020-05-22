def search(array,l,r,elem):
    if(l>=r):
        return False
    mid=(l+r)//2
    # print(l,r,mid)
    if(array[mid]==elem):
        return True
    elif(elem<array[mid]):
        return search(array,l,mid,elem)
    else:
        return search(array,mid+1,r,elem)
    
    


# print(search([9,8,3,2,4],0,4,0))
def main():
    stream=input()
    n,k=map(int,stream.split())
    array=input()
    array=array.split()
    array.sort()
    array=list(map(int,array))
    for x in range(0,n):
        key=k-array[x]
        # print(key)
        if(search(array,0,n-1,key)):
            print('YES')
            return
        
    print('NO')

main()