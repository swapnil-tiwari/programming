table={0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twentyone', 22: 'twentytwo', 23: 'twentythree', 24: 'twentyfour', 
       25: 'twentyfive', 26: 'twentysix', 27: 'twentyseven', 28: 'twentyeight', 29: 'twentynine', 30: 'thirty', 31: 'thirtyone', 32: 'thirtytwo', 33: 'thirtythree', 34: 'thirtyfour', 35: 'thirtyfive', 36: 'thirtysix', 37: 'thirtyseven', 38: 'thirtyeight', 39: 'thirtynine', 40: 'forty', 41: 'fortyone', 42: 'fortytwo', 43: 'fortythree', 44: 'fortyfour',
       45: 'fortyfive', 46: 'fortysix', 47: 'fortyseven', 48: 'fortyeight', 49: 'fortynine', 50: 'fifty', 51: 'fiftyone', 52: 'fiftytwo', 53: 'fiftythree', 54: 'fiftyfour', 55: 'fiftyfive', 56: 'fiftysix', 57: 'fiftyseven', 58: 'fiftyeight', 59: 'fiftynine', 60: 'sixty', 61: 'sixtyone', 62: 'sixtytwo', 63: 'sixtythree', 64: 'sixtyfour', 65: 'sixtyfive',
       66: 'sixtysix', 67: 'sixtyseven', 68: 'sixtyeight', 69: 'sixtynine', 70: 'seventy', 71: 'seventyone', 72: 'seventytwo', 73: 'seventythree', 74: 'seventyfour', 75: 'seventyfive', 76: 'seventysix', 77: 'seventyseven', 78: 'seventyeight', 79: 'seventynine', 80: 'eighty', 81: 'eightyone', 82: 'eightytwo', 83: 'eightythree', 84: 'eightyfour', 85: 'eightyfive',
       86: 'eightysix', 87: 'eightyseven', 88: 'eightyeight', 89: 'eightynine', 90: 'ninety', 91: 'ninetyone', 92: 'ninetytwo', 93: 'ninetythree', 94: 'ninetyfour', 95: 'ninetyfive', 96: 'ninetysix', 97: 'ninetyseven', 98: 'ninetyeight', 99: 'ninetynine', 100: 'hundred'}

vowel='aeiou'
def vowelcounter(string):
    count=0
    for each in vowel:
        count+=string.count(each)
    
    return count
def getVowelSum(arr):
    res=0
    for each in arr:
        res+=each
    return res

def find(arr,l,r,elem):
    if(l<=r):

        mid=(l+r)//2
        if(elem==arr[mid]):
            return mid
        elif(elem<arr[mid]):
            return find(arr,l,mid-1,elem)
        else:
            return find(arr,mid+1,r,elem)
    else:
        return -1

def main():
    N=int(input())
    inp=input()
    inp=inp.split()
    numbers=list(map(int,inp))
    numberVowels=[]
    for each in numbers:
        numberVowels.append(vowelcounter(table[each]))
    
    
    D=getVowelSum(numberVowels)
    if(D==0):
        print("zero")
    
    numbers.sort()
    pair=0

    for x in range(0,len(numbers)):
        key=D-numbers[x]
        if(find(numbers,x,len(numbers)-1,key)!=-1):

            pair+=1
    if(pair>100):
        print("greater 100")
    else:
        print(table[pair])

main()
