stack=[]
def printsubsetsum(sets,sub,n,sum):
    # print(elem)
    
    if(sum==0):
        for each in sub:
            print (each, end=" ")
        print()
        return    
    
    if(n==0):
        return
    # res =  (printsubsetsum(sets,n-1,sum) or (stack.append(sets[n-1]) and printsubsetsum(sets,n-1,sum-sets[n-1])))
    res1=printsubsetsum(sets,sub,n-1,sum)

    sub1=sub
    print(sub,sub1)
    sub1.append(sets[n-1])
    res2=printsubsetsum(sets,sub1,n-1,sum-sets[n-1])

# def main(len):
#     sets=[2, 3, 5, 6, 8, 10]
#     print(printsubsetsum(sets,len,10))
print(printsubsetsum([2,3,5,6,8,10],[],6,10))
# print(stack)

# print(list(map(main,[6,5,4,3,2,1])))

