import sys

def solve(a):
    # Complete this function
    if len(a)==1:
        return "YES"
    sumLeft = a[0]
    sumRight = 0
    for i in range(2,len(a)):
        sumRight = sumRight+a[i]
    for i in range(1,len(a)-1):
        if sumLeft == sumRight:
            return "YES"
        #print(sumLeft," ",sumRight)
        sumLeft = sumLeft+a[i]
        sumRight = sumRight-a[i+1]
    return "NO"

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
