
def sub_list(list):
    counter=0
    subs=[]
    for i in range(len(list)+1):
        for j in range(i+1,len(list)+1):
            subs.append(list[i:j])
            counter+=1

    print("Counter ", counter)
    
    return subs

# sub_list(list)

def max_getter():
    x=int(input())
    array=input()
    res=[]
    array=list(map(int,array.split()))
    subs=sub_list(array)
    for each in subs:
        if (max(each)==x):
            res.append(each)
    return res

# count=len(max_getter())
subs=max_getter()
count=len(subs)
txt="Length is {count} and array is {subs}".format(count=count,subs=subs)
print(txt)

