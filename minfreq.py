def main():
    array=list(map(int,input().split()))
    table={}
    for each in array:
        table[each]=array.count(each)
    count=0
    for each in table:
        if(table[each]!=each):
            temp=table[each]-each
            if(temp>0):
                count+=temp
            else:
                count+=table[each]
    print(table)
    return count

print(main())