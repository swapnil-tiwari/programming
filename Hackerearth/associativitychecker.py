'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def main():
    inp=input()
    c0,c1,c2,c3=map(int,inp.split())

    dict ={'00':str(c0),'01':str(c1),'10':str(c2),'11':str(c3)}
    list=['000','001','010','011','100','101','110','111']
    for each in list:
        x,y,z=map(lambda x: x,each)

        res=dict[x+y]
        ans1=dict[res+z]
        res=dict[y+z]
        ans2=dict[x+res]
        if(ans1!=ans2):
            print('No')
            return
        
    print('Yes')        
           
    

t= int(input())
for _ in range(0,t):
    main()

