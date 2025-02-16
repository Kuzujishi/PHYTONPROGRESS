def main():
   #we will use input("..."): To prompts the user for some text input  
    product_name = input("Enter the product name: ")
   #next we will now put the eval(...): To interpret the text input as a integer in quantity and float in price expression
    quantity = eval(input("Enter the quantity : "))
    unit_price = eval(input("Enter the unit price : "))
    
    #now we will multiply the two values
    total_cost = quantity * unit_price

    #next put some print statements to display a simple receipt that shows total cost in a receipt format and shows the product name,quantity,unit,and price
    print("\n=== Receipt ===")
    print(f"ProductName:{product_name}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: {unit_price}")
    print(f"Total Cost: {total_cost:.2f}")

#lastly lets add if name == "main" to ensure that the code inside it runs only when the script is executed directly, not when imported as a module in another script.

if __name__ == "__main__":
    main()
    
  