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
# def binary_search(arr, target):

#   if len(arr) == 0:
#     return -1 # array empty

#   low = 0
#   high = len(arr)-1

#   # TO-DO: add missing code

#   return -1 # not found


# # STRETCH: write a recursive implementation of Binary Search
# def binary_search_recursive(arr, target, low, high):

#   middle = (low+high)//2

#   if len(arr) == 0:
#     return -1 # array empty
#   # TO-DO: add missing if/else statements, recursive calls
