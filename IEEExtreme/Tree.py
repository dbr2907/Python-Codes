
#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School





t=int(raw_input())
for i in range(t):
    cnt=0
    data=raw_input()
    info=[int(x) for x in data.split(" ")]
    a=info[0]
    b=info[1]

    dn=len(bin(a))-len(bin(b))
    if(dn>0):
        a=a>>dn
    else:
        dn*=-1
        b=b>>dn
    cnt+=dn

    while(a!=b):
        a=a>>1
        b=b>>1
        cnt+=2


    print cnt