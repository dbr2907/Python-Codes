import re
N=int(raw_input())
prices=[]
for k in range(N):
    tmp=raw_input().split()
    for l in range(len(tmp)):
        tmp[l]=int(tmp[l])
    prices.append(tmp)

def matrix(N):
    matriz=[]
    for i in range(N):
        tmp=[]
        for j in range(N):
            tmp.append((1,1,1))
        matriz.append(tmp)
    for i in range(N-1):
        matriz[0][i]=(0,1,1)    
        matriz[N-1][i]=(1,0,1)
        matriz[i][N-1]=(0,0,0)
    matriz[N-1][N-1]=(0,0,0)
    
    return matriz
#bdr 0 = vengo abajo
#bdr 1 = vengo arriba
#bdr 2 = vengo izquierdo

directions=matrix(N)
fin=[N*1000000]

def path(bdr,price,y,x):
    ds=list(directions[y][x])
    if bdr==0:
        ds[1]=0
    elif bdr==1:
        ds[0]=0
    ds=tuple(ds)
    acumulado=price+prices[y][x]
    if(ds==(0,0,0) or acumulado>=fin[0]):
        if acumulado<fin[0]:
            fin[0]=acumulado
    else:
        if(ds[0]==1):
            path(0,acumulado,y-1,x)
        if(ds[1]==1):
            path(1,acumulado,y+1,x)
        if(ds[2]==1):
            path(2,acumulado,y,x+1)
        
for k in range(N):
    path(2,0,k,0)
print fin[0]
