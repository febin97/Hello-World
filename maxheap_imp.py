def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)


def findKlargest(arr,k):
    print(arr[0])
    j=0
    arr2 = []
    for i in range(k-1):
        try:
            arr2.append(arr[2*j+1])
            arr2.append(arr[2*j+2])
        except:
            arr2 = arr2
        n2 = len(arr2)
        for i2 in range(n2, -1, -1):
            heapify(arr2, n2, i2)
        print(arr2[0])
        j = arr.index(arr2[0])
        arr2 = arr2[1:]
    return None       

arr = [44,42,35,33,31,10,26,14,19,27]
n = len(arr)
for i in range(n, -1, -1):
        heapify(arr, n, i)
print(arr)
k = int(input("Enter the Value of k"))
findKlargest(arr,k)
