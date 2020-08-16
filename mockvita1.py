def main():
    n=int(input())
    brides=input()
    grooms=input()
    pairs=n
    head=0
    while(brides!=''):
        flag=0
        pair=pairs
        while(pair):
            
            if(brides[head]==grooms[head]):

                brides=brides.replace(brides[head],'',1)
                grooms=grooms.replace(grooms[head],'',1)
                pairs=pairs-1
                flag=1
                break
            else:
                # groomHead=grooms[0]

                grooms=grooms[1:]+grooms[0:1]
                # print(grooms)
            pair-=1
                
                # grooms=grooms.replace(groom[])
        if(flag==0):
            break
        
    print(pairs)

main()