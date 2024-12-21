n=int(input("Enter No:"))
b=int(input("Base:"))

def BaseToDeci(n,b):
    ans=0
    pow=0
    while n>0:
        r=n%10
        ans+=b**pow*r
        pow+=1
        n=n//10
    print(ans)

BaseToDeci(n,b)
