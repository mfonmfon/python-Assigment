
counter = 1

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))


sum = first_number + second_number 

counter = 0

while counter != sum:

	user_input = input("Do you wan to perform the operation again? ")
	
	counter = counter + 1 
	
	
	if sum == -1:
		print(sum, "continue" )
	else: 
		print("Terminate")

		
