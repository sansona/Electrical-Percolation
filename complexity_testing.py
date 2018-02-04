from union_algorithms import QuickUnion, WeightedQuickUnion, WQU_PathCompression
from random import randint
import matplotlib.pyplot as plt
import timeit

num_unions = 5
range_nodes = 10

def time_test(algorithm):
    t = algorithm(100)
    '''
    for i in range(num_unions):
        t.union(randint(0,range_nodes), randint(0,range_nodes))
    t.connected(randint(0,range_nodes), randint(0,range_nodes))
    '''
    t.union(1,4)
    t.union(2,6)
    t.union(4,3)
    t.union(1,7)
    t.connected(1,3)
    t.union(4,2)
    t.connected(0,2)
    t.connected(1,4)
    t.union(0,3)
<<<<<<< HEAD
    t.connected(0,4)

num_tests = 6
iterations = 100
=======
    t.connected(0,7)
    
num_tests = 2
iterations = 100

test_iterations = []
qu_time = []
wqu_pathcompression_time = []

>>>>>>> 4dbffa167d0a4be7c5f41d8b15857a7cd828e124
print('Quick union implementation:')
for i in range(num_tests):
    test_iterations.append(iterations)
    t = timeit.timeit(stmt="time_test(QuickUnion)",
            setup="from union_algorithms import QuickUnion; from __main__ import time_test",
            number=iterations)
    print('For %s iterations, it takes %.2f seconds' %(iterations, t))
    qu_time.append(t)
    iterations = iterations*10

    if i == num_tests - 1:
        iterations = 100

print('\nWeighted quick union implementation:')
for i in range(num_tests):
    t = timeit.timeit(stmt="time_test(WeightedQuickUnion)",
            setup="from union_algorithms import WeightedQuickUnion; from __main__ import time_test",
            number=iterations)
    print('For %s iterations, it takes %.2f seconds' %(iterations, t))
    iterations = iterations*10

    if i == num_tests - 1:
        iterations = 100

print('\nWeighted quick union with path compression implementation:')
for i in range(num_tests):
    t = timeit.timeit(stmt="time_test(WQU_PathCompression)",
            setup="from union_algorithms import WQU_PathCompression; from __main__ import time_test",
            number=iterations)
    print('For %s iterations, it takes %.2f seconds' %(iterations, t))
    wqu_pathcompression_time.append(t)
    iterations = iterations*10

    if i == num_tests - 1:
        iterations = 100

plt.plot(test_iterations, qu_time, test_iterations, wqu_pathcompression_time)
plt.axis([0, max(test_iterations), 0, max(qu_time)])
plt.ylabel('Time (s)')
plt.xlabel('Number iterations')
plt.show()

