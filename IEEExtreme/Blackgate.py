
#IEEExtreme 11.0
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School


data=[]
pares={}
valores={}
impresion=[]

t=int(raw_input())
for i in range(0,t):
    entrada=raw_input()
    data=entrada.split(" ")
    pares.update({data[0]:int(data[1])})

dsv = sorted(pares.items(), key=lambda x: x[1])


pos = 1
cnt = 0
for x in range(len(dsv)):
    if(x+1 == t):
        break
    else:
        if(dsv[x][1] != dsv[x+1][1]):
            for k in range(pos-1,cnt+pos):
                impresion.append(dsv[k][0])
            impresion.sort()
            
            myStr = ""
            for i in impresion:
                myStr += i + ' '
            myStr += str(pos) + ' ' + str(cnt+pos)
            print myStr

            pos=cnt+pos+1
            impresion= []
        else:
            cnt += 1

for l in range(pos-1,t):
    impresion.append(dsv[l][0])
    impresion.sort()

myStr = ""
for i in impresion:
    myStr += i + ' '
myStr += str(pos) + ' ' + str(t)
print myStr


