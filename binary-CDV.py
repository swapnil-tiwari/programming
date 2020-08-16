def getBinary(num):
    if(num==0):
        return ''
    else:
        return str(num%2) + getBinary(num//2)

def balance(string,factor):
    key=factor-len(string)
    res=string
    for i in range (key):
        res='0'+res
    return res

def convertBinary(number):
    return getBinary(number)[::-1]
def getDig(num):
    import math as m
    return int(m.log(num,2)+1)
def combinations(sets):
    powerset=[]
    from itertools import combinations
    res=0
    for x in range(2,len(sets)+1):

        comb=list(combinations(sets,x))
        # print(comb)
        for each in comb:
            count_0=0
            count_1=0
            for y in range(x):
                # print(each[y])
                count_0+=each[y].count('0')
                count_1+=each[y].count('1')
            if(count_0==count_1):
                res+=1

    return res     


def main():
    N=int(input())
    num=input()
    num=num.split()
    numbers=list(map(int,num))
    maxDig=getDig(max(numbers))
    # print(maxDig)
    # base='0'*maxDig
    binary=list(map(convertBinary,numbers))
    sets=[]
    for each in binary:
        sets.append(balance(each,maxDig))
    
    counter=0
    for each in sets:
        count_1=each.count('1')
        count_0=each.count('0')
        if(count_1==count_0):
            counter=counter+1
    

    counter+=combinations(sets)
    ans=(balance(getBinary(counter),maxDig))

    for each in ans:
        print(int(each),end='')
    # print(ans)
    # print(binary)
    
main()
