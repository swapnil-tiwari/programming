'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import math

# Write your code here
t=int(input())
def ifPower(num,base):
    res=math.log(num,base)
    res=str(res).split('.')[1]
    if(res=='0'):
        return True
    else:
        return False

def money(num):
    # print(num)
    
    if(num==1):
        return True
    if(num>10 and (ifPower(num,10) or ifPower(num,20))):
        
        return True
    if(num!=0 and num%10==0):
        fact1=num//10
        return money(fact1)
    if(num!=0 and num%20==0):
        fact2=num//20
        return money(fact2)    
    
def moneyhack(num):
    # print(num)
    if(num==1):
        return True
    if (num%10==0 and num%20==0):
        fact1=num//10
        fact2=num//20
        if(num==0):
            return moneyhack(fact1)
        else:
            return moneyhack(fact2)
        return moneyhack(num//20)
    elif(num%10==0):
        return moneyhack(num//10)
    elif(num%20==0):
        return moneyhack(num//20)
    
    return False

def main():
    num=int(input())
    # print(money(num))
    if(money(num)):
        print('Yes')
    else:
        print('No')

for _ in range(0,t):
    main()