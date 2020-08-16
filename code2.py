
def main():
  string=input()  
  for j in range(1,len(string)-2):
    if isPalindrome(string[:j]):
      for k in range(j+1,len(string)):
        if isPalindrome(string[j:k]) and isPalindrome(string[k:]):
          print(string[:j])
          print(string[j:k])
          print(string[k:])
          return
  print("Impossible")
def isPalindrome(string):
  l=len(string)
  if l==1:
    return True
  for i in range(l//2):
    if string[i]!=string[-i-1]:
      return False
  return True

main()