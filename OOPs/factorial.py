num=int(input("enter a number: "))
fact=1

if num<0:
    print("factorial doesn't exist")

if num==0:
    print("factorial doesn't exist")

if num>0:
    for i in range(1, num+1):
        fact=fact*i
print("the factorial of given number is",fact)



