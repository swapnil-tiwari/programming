

t=int(input())
  

def coins(n):
    if(n==1):
        return 1
    if(n%2==0):
        n1,n2=n//2,n//2
    else:
        n1,n2=n//2,(n//2)+1
    
    return 1+coins(n2)

  
def main():

    inps=[]
    # n=int(input())
    for _ in range(0,t):
        n=int(input())
        inps.append(n)
    # print(inps)
    for each in inps:
        if(each==2):
            print(2)
        elif(each==1):
            print(1)
        else:
            print(coins(each)-1)

            
        

           

main()


  