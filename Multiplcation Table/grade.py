total = 0
first_total = 0 
second_total = 0
third_total = 0
fourth_total = 0
fifth_total = 0
sixth_total = 0
seventh_total = 0
eight_total = 0
nineth_total = 0
tenth_total = 0
eleventh_total = 0
twelveth_total = 0


#user_input = int(input("Enter a number to loop"))
for first_numbers in range(1,13,1):
    first_value = 1
    first_total += 1
    
  
    for _ in range(1,13,2):
        second_value = 2
        second_total = second_value * first_numbers
        
        for _ in range(1,13,3):
            third_value = 3
            third_total = third_value * first_numbers
          
          
          
            for _ in range(1,13,4):
                fourth_value = 4
                fourth_total = fourth_value * first_numbers
                
                
                for _ in range(1,13,5):
                    fifth_value = 5
                    fifth_total = fifth_value * first_numbers
                    
                    
                    
                    for _ in range(1,13,6):
                        sixth_value = 6
                        sixth_total = sixth_value * first_numbers
                        
                        
                        for _ in range(1,13, 7):
                            seventh_value = 7
                            seventh_total = seventh_value * first_numbers
                            
                            
                            for _ in range(1,13,8):
                                eight_value = 8
                                eight_total = eight_value * first_numbers
                                
                                
                                for _ in range(1,13,9):
                                    nineth_value = 9
                                    nineth_total = nineth_value * first_numbers
                                    
                                    
                                    for _ in range(1,13,10):
                                        tenth_value = 10
                                        tenth_total = tenth_value * first_numbers
                                        
                                        
                                        for _ in range(1,13,11):
                                            eleventh_value = 11
                                            eleventh_total = eleventh_value * first_numbers
                                            
                                            
                                            for _ in range(1,13,12):
                                                twelveth_value = 12
                                                twelveth_total = twelveth_value * first_numbers


    print(f'{first_value} x {first_numbers} = {first_total}\t {second_value} x {first_numbers} = {second_total}\t {third_value} x {first_numbers} = {third_total}\t{fourth_value} x {first_numbers} = {fourth_total} \t{fifth_value} x {first_numbers} = {fifth_total} \t{sixth_value} x {first_numbers} = {sixth_total} \t {seventh_value} x {first_numbers} = {seventh_total}\t {eight_value} x {first_numbers} = {eight_total}\t {nineth_value} x {first_numbers} = {nineth_total}\t {tenth_value} x {first_numbers} = {tenth_total} \t{eleventh_value} x {first_numbers} = {eleventh_total}\t{twelveth_value} x {first_numbers} = {twelveth_total} ')
    
 