# --------------Basic Level-----------

# def hello():
#     print("Hello world")

# hello()

# def add(a,b):
#     print("sum", a+b)

# add(4,9)

# def check_even_odd(a):
#     if a%2==0:
#         print("even")

#     else:
#         print("odd")

# a=int(input("Enter your num: "))
# check_even_odd(a)

# -------------Medium level------------

# def square(m):
#     return n*n

# n=int(input("Enter your num: "))
# print(square(n))

# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact*=i
#     print(fact)

# factorial(5)

# def is_prime(num):
#     if num>1:
#         for i in range(2, num):
#            if num%i==0:
#                return False
#         return True
# print(is_prime(7))


#---------------Advanced ----------------

# def count_digits(num):
#     return(len(str(num)))

# print(count_digits(78906))


def revers_num(a):
    rev=0
    while a>0:
        rev=rev*10 + a%10
        a=a//10
    return rev
print(revers_num(1234))