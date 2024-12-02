a="mango"

print(a[3])   # g
print(a[:4])  # mang  --> same as print(a[0:4])  0 to (n-1) 
              # including 0 but not 4
print(a[4:])  # o   --->that means print(a[4:end])
print(a[2:])  # ngo

print(len(a))  # 5

print(a[-2:-1])   # length-2 : length-1 for positive index  --> g
print(a[-10:-3])   # ma
