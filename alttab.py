def main():
    arr=[1,2,3,4]
    k=2
    pointer=k-1
    while(pointer>0):
        temp=arr[pointer]
        arr[pointer]=arr[pointer-1]
        arr[pointer-1]=temp
        pointer=pointer-1
    print(arr)
main()