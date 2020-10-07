def main():
    # n=int(input())
    # word=input()
    # word=word.split()
    word=["pop","opp","tot","ott","sts","tss","php","hpp","pph"]
    letters=[]
    sort=[]
    for each in word:
        letters=[]
        for let in each:
            letters.append(let)
        letters.sort()
        temp="".join(letters)
        sort.append(temp)
    # print(sort)
    # print(sort.count('opp'))
    hash={}
    for each in sort:
        hash[each]=sort.count(each)
    count = 0 
    for each in hash:
        if(hash[each]>=2):
            count+=1
    # print(hash)
    print(count)
main()