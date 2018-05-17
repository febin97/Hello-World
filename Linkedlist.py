#Rearrange Nodes of a Linked List such that elements at even position comes before odd ones

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

arr = [int(n) for n in input("Enter the elements of the Linked List\n").split(",")]
ls = Node(arr[0])
head  = ls
ls = Node(arr[1])
head.next = ls
for i in range(2,len(arr)):
    ls.next = Node(arr[i])
    ls = ls.next

even = head
odd = head.next

odd_curr = odd
even_curr = even
    
while 1:
    if not even_curr or not odd_curr or not odd_curr.next:
        even_curr.next = odd
        break

    even_curr.next = odd_curr.next
    even_curr = odd_curr.next

    if not even_curr.next:
        odd_curr.next = None
        even_curr.next = odd_curr
        break
    
    odd_curr.next = even_curr.next
    odd_curr = even_curr.next 

while head:
    print(head.data,end="->");
    head = head.next
