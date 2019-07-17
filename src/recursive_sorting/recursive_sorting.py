# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr1, arr2):
    t_len = len(arr1) + len(arr2)
    result = [0] * t_len
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
            k += 1
        else:
            result[k] = arr2[j]
            j += 1
            k += 1
    while (i < len(arr1)):
        result[k] = arr1[i]
        i += 1
        k += 1
    while (j < len(arr2)):
        result[k] = arr2[j]
        j += 1
        k += 1
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if 0 <= len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        arr1 = merge_sort(arr[:mid])
        arr2 = merge_sort(arr[mid:])
        return merge(arr1, arr2)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
