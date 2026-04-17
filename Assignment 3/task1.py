import sys
input = sys.stdin.readline

def merge(a, b):
    result = []
    inversions = 0
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            inversions += len(a) - i  # all remaining elements in a are > b[j]
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result, inversions

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        a1, inv1 = mergeSort(arr[:mid])   # left half
        a2, inv2 = mergeSort(arr[mid:])   # right half
        merged, inv_merge = merge(a1, a2)
        return merged, inv1 + inv2 + inv_merge

n = int(input())
A = list(map(int, input().split()))

sorted_arr, total_inversions = mergeSort(A)

print(total_inversions)
print(*sorted_arr)