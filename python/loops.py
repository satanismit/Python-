# name ="smit"
# for i in name :
#     print(i)

# list=['hello','world','nvidoic']

# for i in list :
#     print(i)
#     for j in i:
#         print(j)

arr=[[1,2],[3],[4],[5,6],"smit",'s']
for i in arr:
     print(i)
    # for j in i:
    #     print(j)


for k in range(10): 
    print(k,end=' ')

print('')

# for k in range(4,9):
#     print(k,end=' ')

print("enter numer table of its number :")
n=int(input())

for k in range(n,n*10+1,n):    # range same as for loop-->for(start , <n*10+1 , n+=n)  
        print(k)    


count=5
while(count>0):
    print(count)
    count-=1
else:
    print("i am in else")

# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==20):
#         break
#     else:
#         print("Mississippi")
# print("Thank you")


# n=int(input("enter one number:"))

# for i in range(10):
    
#     if(i==10):
#         continue
#     print(n," x ",i+1," = ",n*(i+1))
    