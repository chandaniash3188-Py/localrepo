# num=int(input("Enter your number: "))
# fact=1

# if num==1:
#     print("The factorial of 1 is 1")

# elif num==0:
#     print("The fctorial of 0 is 1")

# else:
#     for i in range(2, num+1):
#         fact*=i
#     print("The factorial of {num} is ",fact)


#---------Using Recursion---------

# def fact(num):

#     if num==0:
#         return 1 

#     else:
#         return ((num)*fact(num-1))

# num=int(input("Enter your number: "))

# result=fact(num)
# print(f"The factorial of {num} is {result}")


#-------------Fibonacci Sequence-------------

# num=int(input("Enter your num: "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(1,num+1):
#     c=a+b
#     print(c)
#     a,b=b,c

#----------Number divisible by another-------

print("The number divisible by 13 are: ")

for i in range(1, 100):
    if i%13==0:
        print(i)