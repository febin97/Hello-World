import heapq
from heapq_showtree import show_tree
class Node :
    def __init__(self, data) :
        self.data = data
        self.right = None
        self.left = None
    def PrintTree(self):
        print(self.data)
ls = [int(n) for n in input("Enter the Max heap").split()]
k = int(input("Enter the Value of K"))
h = []
print(heapq.nlargest(k,ls))
show_tree(ls)
