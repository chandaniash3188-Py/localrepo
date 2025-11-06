# efine the menu of cafe
Menu={
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffee":80
}

#Greet
print("Welcome to our restraunt.")
print(" Pizza:Rs 40\n Pasta:Rs50\n Burger:Rs 60\n Salad:Rs 70\n Coffee:Rs 80 ")

Order_total=0

item_1=input("Enter ur name of the item Do u want=")
if item_1 in Menu:
    Order_total += Menu[item_1]
    print(f"Your item {item_1} has been added to yur order")

else:
    print("Ordered item {item_1} is not available")

another_item=input("Do you want to add another item Yes/No = ")
if another_item=="Yes":
    item_2=input("Enter the name of second item= ")
    if item_2 in Menu:
        Order_total += Menu[item_2]
        print(f"Item {item_2} hasbeen added to your order")
    
    # else:
    #     print(f"Ordered item {item_2} is not availabel")

print(f"The total amount of item to pay is {Order_total}")
