def reverse(temp,n):
    print(temp,n)
    if(n!=0):
    
        return reverse(temp*10 +(n%10),n//10)

    else:


        return temp,n

    

print(reverse(0,123))