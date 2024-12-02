b=float(input("enter your mark of subject python :"))
if (b>=75):
    print("Distinction mark..")
elif(60<=b<75):
    print("average mark...")
elif(40<=b<60):
    print("below average mark..")
else  :
    print("you fail..")

c=int(input("enter your age for checking you get any discount or not :"))
if(c>=60):
    print("you got 50% Discount :")
    print("now your ticket :",100-(100*0.5))
elif(18<c<60):
    print("no Discount on ticket..:")
    print("now your ticket :",100)
elif(c<18):
    print("you got 80% Discount on ticket :")
    print("now your ticket :",(100-(100*0.8)))


