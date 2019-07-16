

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
                        number=5, globals=globals())]

c2 = [x2, timeit.timeit(stmt='fn(list2)',
                        number=5, globals=globals())]

c3 = [x3, timeit.timeit(stmt='fn(list3)',
                        number=5, globals=globals())]

c4 = [x4, timeit.timeit(stmt="fn(list4)",
                        number=5, globals=globals())]

c5 = [x5, timeit.timeit(stmt="fn(list5)",
                        number=5, globals=globals())]

coords = [c1, c2, c3, c4, c5]
x_vals = [n[0] for n in coords]
y_vals = [n[1] for n in coords]

plt.scatter(x_vals, y_vals, color="red", marker="*", s=30)
plt.xlabel('input size (n)')
plt.ylabel('time (s)')
plt.title('Merge Sort: Time(s) vs. Input Size(n)')
plt.show()
