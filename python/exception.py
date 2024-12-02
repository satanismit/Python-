try:
    a=int(input("enter one number :"))

    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")

except Exception as e:
    print(e.with_traceback)
    print(e)

finally:
    print("my name is smit satani ..")

print("end of program..")