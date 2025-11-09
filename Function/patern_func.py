# def star(n):
#     for i in range(1,n+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()

# star(5)

# def star(n):
#     for i in range(1,n+1):
#         for j in range(i, n+1):
#             print("*", end=" ")
#         print()

# star(5)


n=5
for i in range(1,n+1):
    for j in range(i, n+1):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()