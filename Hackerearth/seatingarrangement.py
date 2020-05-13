'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def main():
    seat=int(input())
    modfact=seat%12
    fs=0
    if(modfact==0 or modfact == 1):
        if(modfact==0):
            fs=seat-11
        else:
            fs=seat+11
        print(str(fs)+' WS')
    if(modfact==11 or modfact== 2):
        if(modfact==11):
            fs=seat-9
        else:
            fs=seat+9
        print(str(fs)+' MS')
    if(modfact==3 or modfact==10):
        if(modfact==10):
            fs=seat-7
        else:
            fs=seat+7
        print(str(fs)+' AS')
    if(modfact==7 or modfact==6):
        if(modfact==6):
            fs=seat+1
        else:
            fs=seat-1
        print(str(fs)+' WS')
    if(modfact==8 or modfact==5):
        if(modfact==5):
            fs=seat+3
        else:
            fs=seat-3
        print(str(fs)+' MS')
    if(modfact==9 or modfact==4):
        if(modfact==9):
            fs=seat-5
        else:
            fs=seat+5
        print(str(fs)+' AS')

t=int(input())
for x in range(0,t):
    main()    
        
        