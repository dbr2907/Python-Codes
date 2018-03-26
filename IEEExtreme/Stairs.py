#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School



def fib(n):
    a,b = 1,1
    for j in range(n-1):
        a,b = b,a+b
    return a
 
t=int(raw_input())
for i in range(t):
    x=int(raw_input())
    y=fib(x+1)
    print y