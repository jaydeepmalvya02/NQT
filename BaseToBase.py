n=int(input("Enter No:"))
b1=int(input("Base1:"))
b2=int(input("Base2:"))
def BaseToDeci(n,b1):
    ans=0
    pow=1
    while n>0:
        r=n%10
        ans+=pow*r
        pow*=b1
        n=n//10
    return ans

def DeciToBase(t,b2):
    if b2==10:
        return t
    else:
        ans=0
        pow=1
        while t>0:
            r=t%b2
            ans+=pow*r
            pow*=10
            t=t//b2
        return ans

def AnyToAny(n,b1,b2):
    t=BaseToDeci(n,b1)
    ans=DeciToBase(t,b2)
    print(ans)

AnyToAny(n,b1,b2)
