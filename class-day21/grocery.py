# make a function for grocery items , item first name should be captial letter and price should be float value 2 decimal points at the end in the total bill 
def grocery_item(item, **kwargs):
    item = item.capitalize()
    print("Grocery Item:", item)
    total = 0
    for key, value in kwargs.items():
        print(key + " : " + str(value))
        total += float(value)
    print("Total Bill: {:.2f}".format(total))
    return  
    
    # Example call to the function
    grocery_item("apple", price=50, quantity=2) 
    grocery_item("milk", price=120.75, quantity=1)
   