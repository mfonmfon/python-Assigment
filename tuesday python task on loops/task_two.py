
total_scores = 0
scores_counter = 1
scores = 45


while scores_counter <= 15:

	total_scores = total_scores + scores_counter
	scores_counter += 1
	scores = int(input("Enter student scores: "))



	if scores >= 45:

		print("you passed", scores)
	
	else: 
		print("failed")