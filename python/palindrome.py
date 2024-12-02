def palindrom(s):
    s=s[::-1]
    return s

s=input()
n=palindrom(s)
print(s==n)

def fibonaaci(n):
    if n==0:
        print(0)
    if  n==1:
        print(0,1)

    if n==2:
        print(0,1,1)
    else:
        f=0
        f1=1
        f2=1

        for i in range(0,n):
            
            f1=f2
            f2=f1+f2
            print(f2)


    


print(fibonaaci(3))