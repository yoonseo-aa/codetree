n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def insertion_sort(arr):
    for i in range(n):
        j = i -1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

result = insertion_sort(arr)
print(*result)