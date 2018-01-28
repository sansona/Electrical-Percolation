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

iterations = 100
'''
for i in range(5):
    t = timeit.timeit(stmt="time_test(QuickUnion)",
            setup="from union_algorithms import QuickUnion; from __main__ import time_test",
            number=iterations)
    print('For %s iterations, it takes %.2f seconds' %(iterations, t))
    iterations = iterations*10
'''

for i in range(5):
    t = timeit.timeit(stmt="time_test(WeightedQuickUnion)",
            setup="from union_algorithms import WeightedQuickUnion; from __main__ import time_test",
            number=iterations)
    print('For %s iterations, it takes %.2f seconds' %(iterations, t))
    iterations = iterations*10

