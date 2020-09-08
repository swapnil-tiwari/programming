def main():
    inp=input()
    count2=0
    count1=0
    for each in inp:
        if(each == '('):
            count1+=1
        elif(each==')'):
            count2+=1
    if(count1<count2):
        return count1
    else:
        return count2

print(main())