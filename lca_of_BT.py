
class Node :
    def __init__(self, data) :
        self.data = data
        self.right = None
        self.left = None

def printbst(root):
    if root is None:
        return None
    if root.left is not None:
        print(root.left.data,end = "           ")
    if root.right is not None:
        print(root.right.data)
    printbst(root.left)
    printbst(root.right)

def findLCA(root,n1,n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left_lca = findLCA(root.left,n1,n2)
    right_lca = findLCA(root.right,n1,n2)

    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca

def insert(root,list1):
    if list1[i] == "null":
        insert(root,list1[i+1:])
    else:
        root.left.data = list1[i]
    root.data = list1[i]
    insert(root.left,list1[i+1:])
    insert(root.right,list1[i+1:])
    return root  
        
list1 = input().split(",")
i=1
#print(list1[1:])
root = Node(list1[0])
insert(root,list1[1:])
print(root.data)
printbst(root)
print(list1)
print(findLCA(root,4,14).data)
print(findLCA(root,22,14).data)
