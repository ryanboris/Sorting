

import timeit
import matplotlib.pyplot as plt


def fn(arr):
    for i in range(0, len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


x1 = 10
x2 = 1000
x3 = 100000
x4 = 100000000

list1 = [i for i in range(x1)]
list2 = [i for i in range(x2)]
list3 = [i for i in range(x3)]
list4 = [i for i in range(x4)]

c1 = [x1, timeit.timeit(stmt='fn(list1)',
                        number=1, globals=globals())]

c2 = [x2, timeit.timeit(stmt='fn(list2)',
                        number=1, globals=globals())]

c3 = [x3, timeit.timeit(stmt='fn(list3)',
                        number=1, globals=globals())]

c4 = [x4, timeit.timeit(stmt="fn(list4)",
                        number=1, globals=globals())]

coords = [c1, c2, c3, c4]
x_vals = [n[0] for n in coords]
y_vals = [n[1] for n in coords]

plt.scatter(x_vals, y_vals, color="red", marker="*", s=30)
plt.xlabel('input size (n)')
plt.ylabel('time (s)')
plt.title('Time Complexity')
plt.show()
