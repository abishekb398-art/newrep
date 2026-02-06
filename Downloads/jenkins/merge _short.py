def merge_sort(arr):
    # Base case: if list has 1 or 0 elements
    if len(arr) <= 1:
        return arr

    # Find middle point
    mid = len(arr) // 2

    # Divide into two halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Driver code
arr = list(map(int, input("Enter numbers: ").split()))

sorted_arr = merge_sort(arr)

print("Sorted Array:", sorted_arr)
