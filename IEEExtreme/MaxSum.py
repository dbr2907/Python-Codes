#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School



t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    data=raw_input()
    foo=[int(x) for x in data.split(" ")]
    
    foo=foo[1::2]+foo[-1::-2]

print foo