import datetime

print("WELCOME TO SEMICOLON")

customer_name = input("What is the customer name ")

user_response = ""
#list = ()



hours = datetime.datetime.now()


bought_items = input("What did the user buy? ")

numbers_of_bought_items = int(input("How many pieces? "))

price_of_items = int(input("How much per unit? "))
    
add_more_item = input("Do you want to add more items in the cart? ")
    




while add_more_item == "yes":

    bought_items = input("What did the user buy? ")

    numbers_of_bought_items = int(input("How many pieces? "))

    price_of_items = int(input("How much per unit? "))
    
    add_more_item = input("Do you want to add more items in the cart? ")
    


if  add_more_item == "no":
    
    cashiers_name = input("What is your your name (Cashiers name)? ")
    discount = int(input("How much discount will the customer get? "))
   
    
    
    print("SEMICOLON STORES")
    print("MAIN BRANCH")
    
    
    
    print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    
    print("TEL: 0902322232")
    
    print("DATE: ", hours)
  
  
    print("CUSTOMER NAME: ", customer_name)
    print("========================================================")
    
    print("ITEM    \t   QTY    \t  PRICE  \tTOTAL(NGN)")
    
    print("--------------------------------------------------------") 
    print()
    
    total_amount = 0
    subtotal =  0
    vat = 0
    bill_total = 0
    discount = 0
    total_amount = numbers_of_bought_items * price_of_items
    subtotal = total_amount + vat
    discount -= subtotal 
    vat += discount
    
    
    #list.append(bought_items)
    #list.append(numbers_of_bought_items)
   # list.append(price_of_items)
   # list.append(total_amount)

    
    
    #print(list)
    print(f' {bought_items}\t        {numbers_of_bought_items} \t          {price_of_items} \t         {total_amount}')
    print()
    
    print("--------------------------------------------------------")
    print()
    print("========================================================")
    print("\t            Sub Total: ", subtotal)
    print("\t            Discount:  ", discount)
    print("\t            Vat @ 17.50%: ", vat)
    print("==========================================================")
    print("\t            Bill Total:")
    print()
    print("========================================================")
    print("      THIS IS NOT A RECIEPT KINDLY PAY ", bill_total)
    print("========================================================")
    
    print()
    
    amount_paid = int(input("How much did the customer give to you?  "))
    
    balance = amount_paid - bill_total
    
    
   
    print("SEMICOLON STORES")
    print("MAIN BRANCH")
    
    
    
    print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    
    print("TEL: 0902322232")
    
    print("DATE: ", hours)
  
  
    print("CUSTOMER NAME: ", customer_name)
    print("========================================================")
    
    print("ITEM    \t   QTY    \t  PRICE  \tTOTAL(NGN)")
    
    print("--------------------------------------------------------") 
    print()
    
    total_amount = 0
    subtotal =  0
    vat = 0
    bill_total = 0
    discount = 0
    total_amount = numbers_of_bought_items * price_of_items
    subtotal = total_amount + vat
    subtotal = discount - subtotal
    
    
    #list.append(bought_items)
    #list.append(numbers_of_bought_items)
   # list.append(price_of_items)
   # list.append(total_amount)

    
    
    #print(list)
    print(f' {bought_items}\t        {numbers_of_bought_items} \t          {price_of_items} \t         {total_amount}')
    print()
    
    print("--------------------------------------------------------")
    print()
    print("========================================================")
    print("\t            Sub Total: ", subtotal)
    print("\t            Discount:  ",discount)
    print("\t            Vat @ 17.50%: ", vat)
    print("===========================================================")
    print(f'             Bill Total:  {bill_total}    \n   amount paid: {amount_paid}    \n    Balance:  {balance}')
    
    print()
    print("========================================================")
    print("     \t  THIS IS NOT A RECIEPT KINDLY PAY ", bill_total)
    print("=========================================================")
    print("   \t  THANK  YOU FOR YOUR PATRONAGE")
    

    
    
    
    
    
    
    
    
