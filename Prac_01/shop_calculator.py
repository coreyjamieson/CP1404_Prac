"""
A shop requires a small program that would allow them to quickly work out total price for a number of items,
each with different prices.
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen.
"""
running_price = 0
no_of_items = int(input("Enter Number of items: "))
final_price = 0
for i in range (0, no_of_items , 1):
    item = float(input("Enter Item Price:$ "))
    if item <= 0:
        print("Error")
    else:
        print("Price of item:$ ", item)
        running_price = item + running_price

if running_price >= 100:
    final_price = running_price - (running_price * 0.1)
    print("Total price for {} is: ${:.2f}".format(no_of_items, final_price))
else:
    print("Total price for ", no_of_items, "is:$ ", final_price)
