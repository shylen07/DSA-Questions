# Rotate Arry By K

# def rotate(arr,k):
#     return arr[k:] + arr[:k]


# # Driver Code
# array = list(map(int,input().split()))    #array input
# length=len(array)                           #length of an array
# k =int(input())
# ans = rotate( array, k)
# print(ans)


def rotate(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3
k = k % n  # if k is greater than len(arr)
arr = rotate(arr, 0, n - k - 1)
arr = rotate(arr, n - k, n - 1)
arr = rotate(arr, 0, n - 1)

print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
