# STRETCH: implement Linear Search
def linear_search(arr, target):
    '''
    Pseudo/Plan:
      hold reference to current index, i
      while i < len(arr)
        if arr[i] == target
          return index of item found
        else
          increment i by 1 and continue while loop
      endwhile
      return -1 because item was not found upon while loop ending
    '''
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        else:
            i += 1
    return -1


# # STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    '''
    while i < len(arr)
        Find mid element
        if mid == target
            return mid (index of found item)
        if mid < target
            throw out left side (smaller than) mid
            reassign arr to right side
            increment while counter
        if mid > target
            throw out right side (greater than) mid
            reasign arr to left side slice to mid
            increment while counter
    '''
    # l = low
    # h = high
    # m = mid
    arr = sorted(arr)
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == target:
            return m
        if arr[m] > target:
            h = m - 1
        else:
            l = m + 1
    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    arr = sorted(arr)

    if len(arr) == 0:
        return -1

    if not low <= high:
        return -1

    mid = (low + high) // 2

    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return mid
