import math

def isPrime(n):
    for x in range(2,int(math.sqrt(n))+1):
        # print(x)
        if(n%x==0):
            return False
    
    return True


def primegenerator(n1,n2):
    primes=[]
    for x in range (n1,(n2)+1):
        if(isPrime(x)):
            primes.append(x)
    
    return primes
def combinations(list,start,last,combs):
    # print('in')
    if(start<=last):
        for each in range(0,len(list)):
            if(start!=each):

                num=str(list[start])+str(list[each])
                if(isPrime(int(num)) and int(num) not in combs):

                    combs.append(int(num))
        combinations(list,start+1,last,combs)
    
    return combs
        # print(combs)
    
    
def fab(n=1,a=0,b=1):
        while n>1:
                a,b=b,a+b
                n-=1
        else:
                return a

def fib(n,fir,sec):
    if(n==1):
        return fir
    if(n==2):
        return sec+fir
    return fib(n-1,fir,sec)+fib(n-2,fir,sec)
        

def main():
    stream=input()
    n1,n2=map(int,stream.split())
    primes=primegenerator(n1,n2)
    res=combinations(primes,0,len(primes)-1,[])
    # print(len(res))
    fir=min(res)
    sec=max(res)
    n=len(res)
    print(fab(n,fir,sec))
    

    
main()
# res=combinations([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],0,11,[])
# res.sort()
# fir=min(res)
# sec=max(res)


# print(fib(14,3137,6761))
# print(isPrime(17777))