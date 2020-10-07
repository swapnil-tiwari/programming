def main():
    array=input()
    array=list(map(int,array.split()))
    counter={}
    for each in array:
        counter[each]=array.count(each)
    # print(max(counter,key=counter.get))
    return len(array)-counter[max(counter,key=counter.get)]


def custom():
    array=input()
    array=list(map(int,array.split()))
    lastIndex=max(array)
    counter=[0]*(lastIndex+1)
    for each in array:
        counter[each]+=1
    print(counter)
    return len(array)-max(counter)
        
    

print("Res = ",custom())