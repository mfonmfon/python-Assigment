
GAME_NUMBER = 6
for number in range(3):
	game = int(input("Guess the  number "))

	if game == GAME_NUMBER:
		print("you got it broooooo!!!")
		break;
	else:
		print("you failed")
	
