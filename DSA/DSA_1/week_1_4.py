import random
import memory_profiler
from memory_profiler import profile
import time
import matplotlib.pyplot as plt

# @profile
# def sort_list():
#     lst = []
#     for i in range(1, 101):
#         lst.append(i)
#         lst.sort()
    
@profile
def sort_mylist(n):
    lst = []
    for i in range(100):
        lst.append(random.randrange(1, 100, 1))

    #print(lst)

    # Sorting the list.
    lst.sort()

    #print("List Sorted: " +str(lst))


list1 = []
test_list = [i for i in range(100)]


for i in range(1, 101):
    # start = time.perf_counter()
    sort_mylist(test_list[0:i])
    # end = time.perf_counter()
    # final = end - start
    x = memory_profiler.memory_usage()

    list1.append(x[0])
    #print(list1)


plt.plot(test_list, list1)
plt.xlabel('List Length')
plt.ylabel('Space')
plt.title("Space Complexity Graph")
plt.show()