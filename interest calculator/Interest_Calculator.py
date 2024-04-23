amount = int(input("Enter Amount: "))
loan_duration = int(input("Enter loan duration: "))

for i in range(loan_duration):
	RATE = 20 
	RATE_VALUE = RATE / 100
	
	NEW_AMOUNT = RATE_VALUE * amount
	
	total_amount =  NEW_AMOUNT + amount

	amount += NEW_AMOUNT

	print(F'The total interest for {i + 1} #{amount:,.2f}')
	


























#scores = int(input("Enter scores"):

#while score != -1:
	#if scores > pass_mark:
		#number_of_passed += 1
	#else:
		#number_of_failed += 1
	#number_of_students += 1

	#scores = int(input("Enter scores"):
#print(f' the total number is, {number_of_passed}')






#for i in range(10):


	