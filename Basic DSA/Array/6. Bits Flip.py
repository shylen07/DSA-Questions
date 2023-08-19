def kadane(n,arr):
    csum = 0
    msum =0
    for i in range(n):
        csum+=arr[i]
        if csum>msum:
            msum=csum
        if csum <0:
            csum =0
    return max(msum,0)
def maxOnes(n,arr):
    sm = 0
    for i in range(n):
        if arr[i]==1:
            sm +=1
            arr[i] =-1
        else:
            arr[i]= 1
    return sm + kadane(n,arr)

arr =[1,0,0,1,0]
n=len(arr)
print(maxOnes(n,arr))