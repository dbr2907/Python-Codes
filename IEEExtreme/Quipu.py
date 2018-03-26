#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School



import math

def divisorGenerator(w):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(w) + 1)):
        if w % i == 0:
            yield i
            if i*i != w:
                large_divisors.append(w /i)
    for divisor in reversed(large_divisors):
        yield divisor


def quipu(n,d):
    cnt=0
    dd=list(divisorGenerator(n))
    for j in range(len(dd)):
        if(dd[j]%d!=0):
            cnt+=1
    return cnt


data=raw_input()
info=[int(x) for x in data.split(" ")]
t=info[0]
a=info[1]
b=info[2]

for k in range(t):
    rq=0
    d=int(raw_input())
    for l in range(a,b+1):
        rq+=quipu(l,d)
    print rq


