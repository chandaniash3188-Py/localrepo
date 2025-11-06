num=int(input("Enter your num: "))
power=len(str(num))
total=0
for i in str(num):
    total+=int(i)**power
if total==num:
    print(f"The {num} is Armstrong")
       
else:
    print(f"The {num} is Not Armstrong")
       