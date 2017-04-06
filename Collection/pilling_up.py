T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    arr = [int(x) for x in input().split()]
    for i in range(n - 1):
        if (arr[i] >= arr[i + 1]):
            arr[i] = -arr[i]
        else:
            break
    print("Yes" if arr == sorted(arr) else "No")