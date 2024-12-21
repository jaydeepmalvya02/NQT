n=int(input("Enter Number:"))
d=int(input("Digit:"))


def Frequency(n,d):
    ans=0
    r=0
    while n>0:
        r=n%10
        if r==d:
            ans+=1
        n=n//10
    print(ans)

Frequency(n,d)

