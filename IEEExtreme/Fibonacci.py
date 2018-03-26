#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School



def fibR(n):
    if n==1 or n==2:
        return 1
    return fibR(n-1)+fibR(n-2)

t=int(raw_input())
for i in range(t):
    x=int(raw_input())
    y=fibR(x+1)
    out=y%10
    print out
    