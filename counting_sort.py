import random
import time

def counting_sort(array):
    k = max(array)
    counts = [0]*(k+1)
    for x in array:
        counts[x] += 1

    output = []
    for x in xrange(k+1):
        output += [x]*counts[x]

    return output


if __name__ == "__main__":
    assert counting_sort([5,3,2,1]) == [1,2,3,5]
    x = []
    for i in range(0, 1000):
        x.append(random.randint(0, 20))
    assert counting_sort(x) == sorted(x) 
    for i in range(0, 10000000):
        x.append(random.randint(0, 4000))
    start = time.time()
    counting_sort(x)
    end = time.time()
    print "counting sort took: ", end-start
    start = time.time()
    sorted(x)
    end = time.time()
    print "timsort took: ", end-start
