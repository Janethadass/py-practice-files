def count(n):
    c=0
    n=9463
    while(n):
        n=n//10
        c=c+1
        return(c)
    
n=9463;s=0
x=n
c=count(n)
while(n):
    a=n%10
    s=s+a**c
    n=n//10
if(x==s):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
