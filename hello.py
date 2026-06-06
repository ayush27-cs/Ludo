def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        b=i
        while b >0 and arr[b-1]>arr[b]:
            arr[b-1],arr[b] = arr[b],arr[b-1]
            b -= 1



array=[12,13,11,10,5,6,9,8]
print("Original array",array)

insertionsort(array)
print("Sorted array:", array)
