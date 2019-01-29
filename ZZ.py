r=input().split()
a=int(r[0])
b=int(r[1])
i=1
z=[]
d=[]
xx=0
mi=0


for i in range(0,a):
    z.append(int(input()))
xx=mi*b
for i in z:
    j=1
    while 1:
        if j*i>xx:
            break
        else:
            d.append(j*i)
        j+=1
d=list(set(d))
d=sorted(d)

print(d[b-1])







