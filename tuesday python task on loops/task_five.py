number = 5

b = 0

for row in range(number,0 , -1):
	b += 1

	for column in range(1, row + 1):
		print(b, end=" ")

	print(" \r")