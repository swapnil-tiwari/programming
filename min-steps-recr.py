def min2(k,m,n):
    # print(k,m,n)
    d1=k-m
    # print((d1//2)+(d1%2))
    return ((d1//2)+(d1%2))

def minStep(k,m,n):
    if(k>=m):
        return min2(k,m,n)
    else:
        if(m%n==0):
            return 1+minStep(k,m//n,n)
        else:
            return 1+minStep(k,(m//n)+1,n)

def main():
    stream=input()
    k,m,n=map(int,stream.split())
    # print(k,m,n)
    steps=minStep(k,m,n)
    if(k>=m):
        print(steps)
    else:
        print(steps+1)

main()

# 3 31 2


# 3*2=6
# 6-2 4
# 4*2 8
# 8 * 2 16
# 16 * 2 32
# 32 - 1 31
