 
class Node :
    def __init__(self, data) :
        self.data = data
        self.right = None
        self.left = None
    def PrintTree(self):
        print(self.data)
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
    
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
print(root.data)
printbst(root)
root.PrintTree()
print(findLCA(root,4,14).data)
print(findLCA(root,22,14).data)
