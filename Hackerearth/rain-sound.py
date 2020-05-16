'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def main():
    stream=input()
    l,r,s=map(int,stream.split())
    if(s>l and s>r):
        print(-1,-1)
        return
    if(l%s==0):
        min=l//s
    else:

        min=(l//s)+1
    max=r//s
    if(min*s>r):
        print(-1,-1)
        return
    print(min,max)

t=int(input())
for _ in range(0,t):
    main()
