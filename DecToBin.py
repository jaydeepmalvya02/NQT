n=int(input("Enter No:"))
b=int(input("Base:"))
def DecToBin(n,b):
    ans=0
    pow=1

    while n>0:
        r=n%b

        ans+=pow*r
        pow*=10

        n=n//b

    print(ans)

DecToBin(n,b)