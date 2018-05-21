#Check if characters of a given string can be rearranged to form a palindrome
noOfChar = 256
def checkIfPallindrome(str1):
    count = [0] * (noOfChar)            #set all 256 values to zero
    for i in range(len(str1)):
        count[ord(str1[i])] = count[ord(str1[i])]+1
    odd = 0
    for i in range(256):
        if count[i] & 1:
            odd = odd+1
        if odd>1:
            return "No"
    return "Yes"
n = int(input())

while n>0:
    n=n-1
    str1 = input()
    print(checkIfPallindrome(str1))
