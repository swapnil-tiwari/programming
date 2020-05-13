'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
vowel={'a','e','i','o','u','A','E','I','O','U'}
# Write your code here
def vowelfinder(subs):
    vcount=0
    for each in subs:
        for vow in vowel:
            if(each==vow):
                vcount+=1
    return vcount

def substrings(string):
    count=0
    length=len(string)
    for x in range(0,length):
        for i in range (x,length):
            subs=''
            for j in range(x,i+1):
                subs+=string[j]
            count+=vowelfinder(subs)

    return count     
testcases=int(input())

for _ in range(testcases):
    string=input()
    res=substrings(string)
    print(res)
    