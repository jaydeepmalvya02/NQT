n=int(input("Enter Range"))

def PrintZ(n):
    i=1
    while i<=n:
        j=1
        while j<=n:
            if i==1 or i==n or j==n-i+1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
            j+=1
        print()
        i+=1


PrintZ(n)