import random

LUCKY_NUMBER = random.randrange(1,10)
user_input = int(input("Enter the number between 1 and 10:   "))

while LUCKY_NUMBER != user_input:
	
		user_input = int(input("Guess the  number between 1 - 10:    "))

		
		if user_input == LUCKY_NUMBER :
			print("you got it broooooo!!!")
			break;

		elif user_input > LUCKY_NUMBER:
			print("Opoos! looks like you entered a  number above 1 - 10")
			break;
		else:
			print("you failed")

		print(LUCKY_NUMBER)

