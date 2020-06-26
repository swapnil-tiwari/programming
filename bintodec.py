# Recursive way to convert a binary number to decimal
print("Enter Number in Binary form: ")
num=int(input())
def converter(num):
    if(len(str(num))==1):
        return num
    val=converter(num//10)*2+num%10
    return val

print(converter(num))
