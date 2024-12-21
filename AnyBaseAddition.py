d1=int(input("Enter  first Digit:"))

d2=int(input("Enter second Digit:"))

b=int(input("Base:"))

def BaseAdd(d1,d2,b):
    ans=0
    carry=0
    pow=1
    while d1 >0 or d2>0 or carry>0:
        r1=d1%10
        r2=d2%10
        digit=r1+r2+carry
        carry=digit//b
        digit=digit%b

        ans+=pow*digit
        pow*=10
        d1=d1//10
        d2=d2//10
    print(ans)
BaseAdd(d1,d2,b)