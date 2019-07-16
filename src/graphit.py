

import random
import timeit
import matplotlib.pyplot as plt


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


ipt = input('1 - selection\n2 - bubble\n3 - merge\n')

if ipt == '1':
    def fn(arr):
        for i in range(0, len(arr) - 1):
            smallest = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[smallest]:
                    smallest = j
            arr[i], arr[smallest] = arr[smallest], arr[i]

        return arr


if ipt == '2':
    def fn(arr):
        last_index = len(arr) - 1
        swaps_performed = True
        while swaps_performed:
            swaps_performed = False
            for i in range(last_index):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swaps_performed = True
        return arr


if ipt == '3':
    def fn(arr):
        if 0 <= len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            arr1 = fn(arr[:mid])
            arr2 = fn(arr[mid:])
            return merge(arr1, arr2)


x1 = 1
x2 = 1200
x3 = 4000
x4 = 7000
x5 = 10000

list1 = [i for i in range(x1)]
list2 = [i for i in range(x2)]
list3 = [i for i in range(x3)]
list4 = [i for i in range(x4)]
list5 = [i for i in range(x5)]

random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)
random.shuffle(list5)

c1 = [x1, timeit.timeit(stmt='fn(list1)',
                        number=2, globals=globals())]

c2 = [x2, timeit.timeit(stmt='fn(list2)',
                        number=2, globals=globals())]

c3 = [x3, timeit.timeit(stmt='fn(list3)',
                        number=2, globals=globals())]

c4 = [x4, timeit.timeit(stmt="fn(list4)",
                        number=2, globals=globals())]

c5 = [x5, timeit.timeit(stmt="fn(list5)",
                        number=2, globals=globals())]


coords = [c1, c2, c3, c4, c5]
x_vals = [n[0] for n in coords]
y_vals = [n[1] for n in coords]

plt.scatter(x_vals, y_vals, color="red", marker="*", s=30)

if ipt == '1':
    plt.title('Selection Sort: Time(s) vs. Input Size(n)')
if ipt == '2':
    plt.title('Bubble Sort: Time(s) vs. Input Size(n)')
if ipt == '3':
    plt.title('Merge Sort: Time(s) vs. Input Size(n)')

plt.xlabel('input size (n)')
plt.ylabel('time (s)')
plt.show()
