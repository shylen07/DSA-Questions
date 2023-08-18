#max subarray sum
def kadane(arr,n):
    current_sum ,max_sum = 0,0
    for i in range(n):
        current_sum +=arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum =0
    return max_sum
arr=[-1,2,-2,5,7,-3,1]
n =len(arr)
ans = kadane(arr,n)
print(ans)

    