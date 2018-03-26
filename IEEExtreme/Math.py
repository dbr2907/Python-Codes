#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School



import math


    

t=int(raw_input())
for i in range(t):
    data=raw_input()
    info=[int(x) for x in data.split(" ")]
    a=info[0]%((10**9)+7)
    if a!=1:
        b=info[1]%((10**9)+7)
        c=info[2]%((10**9)+7)
        d=(b-c)%((10**9)+7)     
        if(d!=0):
            o1=math.factorial(c)
            o2=math.factorial(d)
            o3=math.factorial(b)
            res=(o3/(o2*o1))
            y=int(a**res)%((10**9)+7)
        else:
            y=a
        print y
    else:
        print 1