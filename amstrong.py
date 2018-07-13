x=int(input())
s=0
t=x
while t>0:
       a=t% 10
       s=s+(a**3)
       t=t//10
if x==s:
		print("yes")
else:
        print("no")
