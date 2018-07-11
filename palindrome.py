a=int(input())
temp=a
rev=0
while(n>0):
    dig=a%10
    rev=rev*10+dig
    rev=a//10
if(temp=rev):
    print("number is palindrome")
else:
    print("number is not palindrome")
