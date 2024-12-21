d1=int(input("Enter First No:"))
d2=int(input("Enter Second No:"))

b=int(input("Enter Base:"))

def BaseSub(d1,d2,b):
    ans=0
    carry=0
    pow=1
    while  d2>0 or carry>0:
        r1=(d1%10)
        r2=(d2%10)+carry

        if r2-r1>=0:
            digit = r2 - r1
            carry=0
        else:
            carry=-1
            digit=d2+b-d1

        ans+=pow*digit
        pow*=10
        d1=d1//10
        d2=d2//10
    print(ans)
BaseSub(d1,d2,b)