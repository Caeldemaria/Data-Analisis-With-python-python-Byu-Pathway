# Start code reading the document
with open("life-expectancy.csv") as life_expectancy:
    # Ask for an year for the search
    year_interes=int(input("Enter the year of interest: "));
    # varibles to find the min and the max number in all data and varibles to put the  future information 
    min_life=999
    max_life=0
    entity_max=''
    entity_min=''
    year_min=0
    # varibles to make equasion of avarage off the year that had ask before
    Avarage=0
    count=0
    totalLife=0
    # varables to help put information about the min and max about the year that had asnk before
    entity_interest_max=""
    entity_interest_min=""
    max_interes=0
    min_interes=9999
    # this line help to ignore the title
    next(life_expectancy)
    # loop for all code. this will help to make the funtions
    for line in life_expectancy:
        #Split eache line and transkor the data. years and life change the type for numbers
        data=line.split(",")
        entity=data[0]
        code=data[1]
        years=int(data[2])
        life=float(data[3])
        # condition to find the max
        if life> max_life:
            max_life=life
            year_max=years
            entity_max=entity
    
    # condition to find the min
        if life<min_life:
            min_life=life
            year_min=years
            entity_min=entity
            #this part will work with the year tha had ask before this condition make max and min, and Avarege of the life Expectancy
        if years==year_interes:
            if life> max_interes:
                max_interes=life
                entity_interest_max=entity
            if life<min_interes:
                min_interes=life
                entity_interest_min=entity
            totalLife+=life
            count+=1
            
    Avarage=totalLife/count
# this all print. this follow the script and layout 
    
    print(f"The overall max life expectancy is:{max_life} from {entity_max} in {year_max}")
    print(f"The overall min life expectancy is:{min_life} from {entity_min} in {year_min}")
    print()
    
    print(f"For the year {year_interes}: ")
    print(f"The average life expectancy across all countries was {Avarage:.2f}")
    print(f"The max life expectancy was in {entity_interest_max} with {max_interes}")
    print(f"The min life expectancy was in {entity_interest_min} with {min_interes}")



