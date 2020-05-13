'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import math    
def binsearch(l,r,num):
    mid=(l+r)//2
    # print (mid)
    res=num//mid
    if(l==r):
        return mid
    elif(res.bit_length()<=mid.bit_length()):
        return binsearch(l,mid,num)
    
    else:

        return binsearch(mid+1,r,num)
       
def qfFinder(num,div):
    qf=num//div
    if(qf.bit_length()==div.bit_length()):
        return div
    else:
        return qfFinder(num,div+1)

# print(qfFinder(3,1))
def main():
    num=int(input())
    r=int(math.sqrt(num))
    # print(num)
    print((num-(binsearch(1,r+2,num)))+1)
    # divs=[i for i in range(1,int(math.sqrt(num)+2))]
    # print(divs)
    # print((num-qfFinder(num,int(math.sqrt(num))))+2)
    # if(num%2!=0):

    #      print((num-int(math.sqrt(num)))+1)
    # else:
        
    #      print((num-int(math.sqrt(num))))

t=int(input())
for _ in range(t):
    main()