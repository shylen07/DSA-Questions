# Count pair whose sum equal to target

def pairSum(arr, n, target):
    i=0
    j=n-1
    count = 0
    while i < j:
        if arr[i]+arr[j] == target:
            count+=1
            i+=1
            j-=1
        elif arr[i]+arr[j] > target:
            j-=1
        elif arr[i]+arr[j] < target:
            i+=1
    if count ==0:
        return -1
    return count

