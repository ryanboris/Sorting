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
    arr = sorted(arr)
    if len(arr) == 0:
        return -1
    i = 0
    while i < len(arr):
        low = 0
        high = len(arr) - 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] > target:
                arr = arr[:mid]
                i += 1
            else:
                arr = arr[mid:]
                i += 1
    return -1


print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], -2))

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
