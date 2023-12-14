def binarySearch(target, arr) -> int:
    
    (left, right) = (0, len(arr) - 1)
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == "__main__":
    arr = [2,3,4,7,8]
    target = 9
    print(binarySearch(target, arr))

