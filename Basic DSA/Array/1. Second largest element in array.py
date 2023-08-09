# Find second largest element in an array.
# Note : Duplicates may be present , If no such element is present return-1
def secondElement(n,arr):
    largest = float('-inf')
    second = float('-inf')
    for i in range(n):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i]>second and arr[i]<largest:
            second =arr[i]
    if second == float('-inf'):
        return -1
    return second

array = list(map(int,input().split()))    #array input
length=len(array)                              #length of an array
ans = secondElement(length , array)
print(ans)

