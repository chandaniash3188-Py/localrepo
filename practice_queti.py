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

# print("The number divisible by 13 are: ")

# for i in range(1, 100):
#     if i%13==0:
#         print(i)

#----------using lambda and filter function---------

# l=[39,48,26,98,33,67,87]

# result=list(filter(lambda x:x%13==0,l))
# print(result)


#---------find HCF--------

# def findHCF(x,y):
#     hcf=1
#     for i in range(1, min(x,y)+1):
#         if x%i==0 and y%i==0:
#             hcf=i
#     return hcf

# print("The hcf of the given two number is", findHCF(12,30))


# import calendar
# year=int(input("Enter the year: "))
# month=int(input("Enter the month: "))

# calendar=calendar.month(year, month)
# print(calendar)


#---------Fibonacci using Recursion---------
def fibonacci(n):
    if n<0:
        return "Invalid input"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(num):
    print(fibonacci(i))