
def findSum(B, k):
    A = mergeSort(B)
    left = 0
    right = len(A) - 1
    while left < right:
        if A[left] + A[right] == k:
            return True
        elif A[left] + A[right] < k:
            left += 1
        else:
            right -= 1
    return False

def mergeSort(A):
    if(len(A) == 1):
        return A

    midIndex = len(A) // 2
    left = mergeSort(A[:midIndex])
    right = mergeSort(A[midIndex:])
    return merge(left, right)

def merge(left, right):
    combined = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1

    while i < len(left):
        combined.append(left[i])
        i += 1

    while j < len(right):
        combined.append(right[j])
        j += 1

    return combined

test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(findSum(test, 17))

