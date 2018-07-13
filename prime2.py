x=int(input())
y=int(input())
c=0
for n in range(x+1,y+1):
    for i in range(1,n+1):
        if(n%i)==0:
            c=c+1
    if(c==2):
        print(n)
    c=0
