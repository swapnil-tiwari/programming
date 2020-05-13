import math
def steps(start,array,end):
    if(len(array)==2):
        return abs(array[end]-array[start])
    if (start==end):
        return 0
    else:

            
        jFactor1=abs(array[start]-array[start+1])
        jFactor2=abs(array[start]-array[start+2])
        if(jFactor2==jFactor1):
            return jFactor1+steps(start+2,array,end)
        if(jFactor1<jFactor2):
            return jFactor1+steps(start+1,array,end)
        else:
            return jFactor2+steps(start+2,array,end)

    


array=[10, 30,40,60,50]
print(steps(0,array,4))