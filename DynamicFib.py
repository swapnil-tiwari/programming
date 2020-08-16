def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        
        return fib(n-1)+fib(n-2)

# print(fib(10))
print("Enter n: ")
n=int(input())
t=[-1]*(n+1)
t[0]=0
t[1]=1
def fib_dyn(n):
    
        if(t[n]==-1):
            t[n]=fib_dyn(n-1)+fib_dyn(n-2)
            return t[n]
        else:
            return t[n]

print(fib_dyn(n))
print(t)