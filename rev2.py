a=int(input())
r=0
while(a>0):
		d=a%10
		r=r*10+d
		a=a//10
print(r)
