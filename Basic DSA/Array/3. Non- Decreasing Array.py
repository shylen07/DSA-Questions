def isPossible(arr, n):
    count = 0
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            count +=1
            if count > 1:
                return False
            elif i ==1 or arr[i] >=arr[i-2]:
                arr[i - 1] = arr[i]
            else:
                 arr[i] = arr[i - 1]
        
tc = int(input())
while tc > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = isPossible(arr, n)
    print('true') if ans else print('false')
    tc -= 1