#Delete Duplicate elements from a sorted array

arr = [int(x) for x in input("Enter the sorted array\n").split(",")]
item = arr[0]
n = len(arr)
i=0
j=1
while i < len(arr):
    print(i ,arr[i],item,len(arr))
    print(arr)
    i=i+1
    if arr[i] == item:
        i=i+1
        while arr[i] == item :
            i=i+1
            if i == len(arr):
                break
        if i< len(arr):
            item = arr[i]
            arr[j] = arr[i]
            j=j+1
    else:
        item = arr[i]
        arr[j]  = item
        j=j+1
        
print(arr[:j])
