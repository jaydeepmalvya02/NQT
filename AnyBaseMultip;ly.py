d1=int(input("enter  first digit:"))
d2=int(input("Enter Second Digit:"))
b=int(input("Enter Base:"))



def Sumofno(d1,d2,b):
    ans = 0
    carry = 0
    pow = 1
    while d1 > 0 or d2 > 0 or carry > 0:
        r1 = d1 % 10
        r2 = d2 % 10
        digit = r1 + r2 + carry
        carry = digit // b
        digit = digit % b

        ans += pow * digit
        pow *= 10
        d1 = d1 // 10
        d2 = d2 // 10
    return ans

def SingleMul(b,d1,r2):

    ans=0
    c=0
    p=1

    while d1>0 or c>0:

        r1 = d1 % 10
        d1 = d1 // 10
        d = r1 * r2+c
        c=d//b
        d=d%b
        ans+=p*d
        p*=10
    return ans


def AnyBaseMul(d1,d2,b):
    ans=0
    p=1
    while d2>0:
        r2=d2%10
        d2=d2//10
        pro=SingleMul(b,d1,r2)
        ans=Sumofno(ans,pro*p,b)
        p*=10
    print(ans)








AnyBaseMul(d1,d2,b)