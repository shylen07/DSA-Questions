def pairSum(arr, start, end, i, target):
    new_target = target - arr[i]
    while start < end:
        sm = arr[start] + arr[end]
        if sm == new_target:
            return arr[start], arr[end]
        elif sm > new_target:
            end -= 1
        elif sm < new_target:
            start += 1
    return False

def pair(arr, start, end, i, target):
    ans = pairSum(arr, start, end, i, target)
    if ans == False:
        return 
    else:
        a, b = ans
        c = target - (a + b)
        print(a, b, c)

arr = [1, 2, 3, 4, 5]
target = 10
arr.sort()
n = len(arr)
for i in range(n - 2):
    start = i + 1
    end = n - 1
    pair(arr, start, end, i, target)
