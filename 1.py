import math, operator


n=1000
fd = dict()
fd['√log4n'] = math.sqrt(math.log(n, 4))
fd['(log2n)^log2n'] = math.log(n, 2)**math.log(n, 2)
fd['(log2n)^2'] = math.log(n, 2)**2
fd['n^log2n'] = n**math.log(n, 2)
fd['n^2'] = n**2
fd['√n'] = math.sqrt(n)
fd['3^log2n'] = 3**math.log(n, 2)
fd['log2(log2n)'] = math.log(math.log(n, 2))
fd['log3n'] = math.log(n, 3)
fd['n^√n'] = n**math.sqrt(n)
fd['n/log5n'] = n/math.log(n, 5)
fd['7^(log2n)'] = 7**math.log(n, 2)
fd['2^n'] = 2**n
fd['2^(3n)'] = 2**(3*n)
#fd['2^(2^n)'] = 2**(2**n) // по моим подсчетам это выражение считаеся 100500 лет, для экономии времени закомментируем
fd['4^n'] = 4**n
fd['log2(n!)'] = math.log(math.factorial(n), 2)
fd['n!'] = math.factorial(n)
 
#print({k: v for k, v in sorted(fd.items(), key=lambda item: item[1])})
i = 0
for v in sorted(fd, key=fd.get):
    i += 1
    print(i, v, fd[v])