'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
def main():
    stream=input()
    N,M=map(int,stream.split())
    virus=[0 for _ in range(0,N)]
    for _ in range(0,M):
        inp=input()
        L,K,P=map(int,inp.split())
        for x in range(L-1,K):
            virus[x]+=P
        # print(virus)
    res=0
    for each in virus:
        res=res^each
    print(res)    

t=int(input())
for _ in range(0,t):
    main()
