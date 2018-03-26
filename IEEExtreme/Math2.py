#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School




memo={}

def fact(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    else:
        z = (fact(n-1) * n)%((10**9)+7)
        memo[n] = z
        return z
    
def f3(lma,lme):
    f=1
    if lme!=0:
        for l in range(lme,lma):
            f*=(l+1)%((10**9)+7)
    return (f%((10**9)+7))
        
    

t=int(raw_input())
for i in range(t):
    data=raw_input()
    info=[int(x) for x in data.split(" ")]
    a=info[0]%((10**9)+7)
    if a!=1:
        b=info[1]%((10**9)+7)
        c=info[2]%((10**9)+7)
        d=b-c
        
        if(d!=0):
            if(d<c):
                mn=fact(d)
                sec=f3(b,c)
                res=sec/mn
            else:
                mn=fact(c)
                sec=f3(b,d)
                res=sec/mn
            
            y=a**res
        else:
            y=a
        print y%((10**9)+7)
    else:
        print 1