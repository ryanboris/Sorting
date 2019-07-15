def selection_sort(arr):
    '''
    Plan/Pseudocode:
        iterate over the arr once to capture each item
            store current item in var
            iterate over arr again to capture item next to first
                compare first item to corresponding second item
                if second item < first item
                    reassign current item to second item
                if second item > first item
                    do nothing and keep original var assigned to first item
            enditerate
            swap original item with smallest item
        enditerate
        return arr

    '''
    for i in range(0, len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr


# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):

#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
