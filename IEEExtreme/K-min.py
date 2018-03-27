vec=[]
sm=[]

tmp=raw_input().split()
N=int(tmp[0])
M=int(tmp[1])
K=int(tmp[2])
vec=raw_input().split()
for i in range(N):
    vec[i]=int(vec[i])

for i in range(M-1):
    vec.append(vec[i])
    
def Kmin(vecs,k):
    vecs.sort()
    return vecs[k-1]

mini=2147483647

for j in range(N):
    ls=vec[j:j+M]
    tmp=Kmin(ls, K)
    if(tmp<mini):
        mini=tmp

print mini
        


