from itertools import permutations

def opsimul(intlist):
    for intset in permutations(intlist): #intset = one perm of ints
        results = [] #initialize results list
        for x in intset: #x = a number in intset
            tmp = [] #initialize tmp list
            while results: #while results list is not empty
                previous = results.pop(0) #results[0]
                tmp.append(previous + '+' + str(x*1.0))
                tmp.append(previous + '-' + str(x*1.0))
                tmp.append(previous + '*' + str(x*1.0))
                tmp.append(previous + '/' + str(x*1.0))
            if tmp == []: #when tmp is empty
                tmp.append(str(x*1.0))
            results = tmp[:] #set result = tmp
        return results

def opfilter(intlist, final):
    explist = opsimul(intlist)
    doc = open('results.txt', 'w') #open & write to results.txt
    for exp in explist:
        if eval(exp) == final:
            doc.write(exp + ' = ' + str(eval(exp)) + '\n')
    doc.close()
    
opfilter(range(1,6), 6)

"""
permutations function
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
"""