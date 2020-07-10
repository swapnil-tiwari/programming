def encrypter(msg):
    # print(msg)
    mid=len(msg)//2
    if(mid<=0):
        return msg
    else:
        if(not len(msg)%2):
            mid=mid-1
            return msg[mid] + encrypter(msg[:mid]) + encrypter(msg[mid+1:])
            # print(msg[mid-1])
            
            
        else:
            # print(msg[mid])
            # encrypter(msg[:mid])
            # encrypter(msg[mid+1:])
            return msg[mid] + encrypter(msg[:mid]) + encrypter(msg[mid+1:])



def main():
    msg=input()
    print(encrypter(msg))

main()