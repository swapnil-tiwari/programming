'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
def min2(k,m,n):
    # print(k,m,n)
    d1=k-m
    # print((d1//2)+(d1%2))
    return ((d1//2)+(d1%2))


def main():
    inp=input()
    res=0
    inp=inp.split()
    k=int(inp[0])
    m=int(inp[1])
    n=int(inp[2])
    if(k>m):
        res=min2(k,m,n)
        # d1=k-m
        # d1=d1//2
        # res=d1+(d1%2)
    else:
        qf=m//n
        if(k==qf):
            res=1
        if(qf<k):
            res=min2(k,qf,n)+1
        if(qf>k):
            if(qf//k==n):
                res=1+1
                print('inhere')
            else:
                mf=k*n
                # print(mf)
                res=1
                while(mf<qf):
                    mf=mf*n
                    # print('nn')
                    res=res+1
                # print(min2(mf,qf,n))
                res+=min2(mf,qf,n)+1
    print(res)




for x in range(0,t):
    main()

# for x in range(0,t):
#     inp=input()
#     res=0
#     inp=inp.split()
#     k=int(inp[0])
#     m=int(inp[1])
#     n=int(inp[2])
#     if(k>m):
#         d1=k-m
#         d1=d1//2
#         res=d1+(d1%2)
#     else:
