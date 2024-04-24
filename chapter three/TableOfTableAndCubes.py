print("numbers\t Squares \tCubes ")
squares = 0
cubes = 0
for numbers in range(6):
	squares += numbers + 2
	cubes += squares + 1
	print(f'{numbers} \t   {numbers * numbers}\t         {numbers * numbers * numbers}')

