from union_algorithms import QuickUnion, WeightedQuickUnion
import timeit

def time_test(algorithm):
    t = algorithm(100)
    t.union(1,2)
    t.connected(1,2)
    t.union(4,2)
    t.union(3,4)
    t.connected(0,2)
    t.connected(1,4)
    t.union(0,3)
    t.connected(0,4)

num_tests = 6
iterations = 100
print('Quick union implementation:')
for i in range(num_tests):
    t = timeit.timeit(stmt="time_test(QuickUnion)",
            setup="from union_algorithms import QuickUnion; from __main__ import time_test",
            number=iterations)
    print('For %s iterations, it takes %.2f seconds' %(iterations, t))
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

