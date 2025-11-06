#----------Prime num or not----------

num = int(input("enter ur num: "))

if num == 1:
    print("it is not prime num")

elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("it is not prime num")
            break
    else:
        print("it is prime num")


# Python program to check if a number is prime using a for loop

# num = int(input("Enter a number: "))

# # All numbers less than 2 are not prime
# if num <= 1:
#     print(num, "is not a prime number")

# else:
#     # Loop from 2 to num-1
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         # This else runs only if the loop didn't break
#         print(num, "is a prime number")
    



# Lower = int(input("Enter lower range: "))
# Upper = int(input("Enter upper range: "))

# for num in range(Lower, Upper+1):
#     for i in range(2, num):
#         if num % i == 0:
#             # print(num, "is not a prime number")
#             break
#     else:
#         print(num)


# Lower = int(input("Enter lower range: "))
# Upper = int(input("Enter upper range: "))

# for num in range(Lower, Upper+1):
    
#         if num % 2 == 1:
#             print(num)
            

# n=int(input("Enter a number : "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")