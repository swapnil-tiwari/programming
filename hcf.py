
def hcf(n1,n2):
    if(n2==0):
        return n1
    else:
        return hcf(n2,n1%n2)

# print(hcf(n1,n2))
def main():
    n1=int(input())
    n2=int(input())
    res=hcf(n1,n2) if n1>n2 else hcf(n2,n1)
    print(res)
main()

