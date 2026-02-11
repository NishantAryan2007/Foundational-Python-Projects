    #  DECIDING THE MENU
menu = {
    'PIZZA':100,
    'PASTA':80,
    'SAMOSA':20,
    'ICE-CREAM':50,
    'CHOCOLATE':10,
}
#Greet
print("WELCOME TO EXQUISITE RESTAURANT")
#Providing menu to the customer.
print("PIZZA : Rs.100\nPASTA : Rs.80\nSAMOSA : Rs.20\nICE-CREAM : Rs.50\nCHOCOLATE : Rs.10")
total_price=0
order_1=input("ENTER THE FOOD YOU WANT TO ORDER : ").upper()
if order_1 in menu:
    total_price+=menu[order_1]
    print(f"YOUR {order_1} is added to the list.")
else:
    print(f"SORRY {order_1} is not available with us yet.")
order_2=input("WOULD YOU LIKE TO ORDER SOMETHING ELSE? (YES/NO):").upper()
if order_2 == "YES":
    item_2=input("ENTER YOUR SECOND ORDER : ").upper()
    if item_2 in menu:
        total_price+=menu[item_2]
        print(f"YOUR {item_2} is added to the list.")
    else:
        print(f"SORRY {item_2} is not available with us yet.")
print(f"THE TOTAL AMOUNT TO BE PAID IS Rs.{total_price}")    
print("THANK YOU FOR VISITING. DO COME AGAIN !!")            


