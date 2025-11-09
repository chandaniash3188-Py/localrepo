# num=int(input("Enter yur num: "))

# sum=0
# temp=num
# power=len(str(num))

# while temp>0:
#    digit=temp%10
#    sum+=power
#    temp//=10

# if sum==num:
#     print("It is armstrong num")

# else:
#     print("It is not")



# lower=int(input("Enter your lower range: "))
# upper=int(input("Enter your upper range: "))


# for num in range(lower, upper+1):
#    power=len(str(num))
#    sum=0
#    temp=num
#    while num>0:    
#       digit=temp%10
#       sum+=digit**power
#       temp//=10
        
# if sum==num:
#     print(num)
        


num=int(input("Enter your num: "))
sum=0
while num>0:
    sum+=num
    num-=1
print(sum)


       