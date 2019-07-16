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


def bubble_sort(arr):
    '''
    Plan/Pseudo:
        swaps_performed
        while swaps_performed
            not swaps_performed
            iterate over arr
                if arr[i] > arr[arr i + 1]
                    swap arr[i] and arr[i+1]
                    swaps_performed -> back to [0] to repeat
            enditerate
        endwhile
    '''
    last_index = len(arr) - 1
    swaps_performed = True
    while swaps_performed:
        swaps_performed = False
        for i in range(last_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_performed = True
    return arr


#  STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    m = maximum + 1
    count = [0] * m

    for num in arr:
        count[num] += 1

    i = 0
    for n in range(m):
        for j in range(count[n]):
            arr[i] = n
            i += 1
    return arr
