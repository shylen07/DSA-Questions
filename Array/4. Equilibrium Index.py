# def Equilibrium(arr,n):
#     j=n-1
#     sm1 = 0
#     sm2 = 0
#     for i in range(n):
#         sm1 +=arr[i]
#         if sm1 == sm2:
#             return i+1
#         sm2 +=arr[j]
#         j-=1
#     return -1




def equilibrium_sum(arr):
    n = len(arr)
    total_sum = sum(arr)
    left_sum = 0

    for i in range(n):
        total_sum -= arr[i]

        if left_sum == total_sum:
            return i

        left_sum += arr[i]

    return -1

# Test the function

arr = [18, 2 ,12, 2 ,18]
n = len(arr)
print(equilibrium_sum(arr))
