from config import config 


class utils:
 
    def total_dog(number_small_dogs,number_medium_dogs,number_large_dogs):
        total_dog = number_small_dogs+number_medium_dogs+number_large_dogs
        return(total_dog)
        
            

    def amount_of_food_small_dog(number_small_dogs):
        amount_of_food_small_dog = number_small_dogs * config.small_dog
        if amount_of_food_small_dog >= 0:
           return(amount_of_food_small_dog)
        else:
            raise ValueError("Value is less than zero")
        

    def amount_of_food_medium_dog(number_medium_dogs):
        amount_of_food_medium_dog = number_medium_dogs * config.medium_dog
        if amount_of_food_medium_dog >= 0:
           return(amount_of_food_medium_dog)
        else:
            raise ValueError("Value is less than zero")

    def amount_of_food_large_dog(number_large_dogs):
        amount_of_food_large_dog = number_large_dogs * config.large_dog
        if amount_of_food_large_dog >= 0:
           return(amount_of_food_large_dog)
        else:
            raise ValueError("Value is less than zero")   
    
    def amount_of_food(amount_of_food_small_dog, amount_of_food_medium_dog, amount_of_food_large_dog):
        amount_of_food = int(amount_of_food_small_dog + amount_of_food_medium_dog + amount_of_food_large_dog )
        return(amount_of_food)     

    def amount_of_food_with_Xpercentage(amount_of_food):
        amount_of_food_with_Xpercentage = float(amount_of_food * config.extraPercentage)
        return(amount_of_food_with_Xpercentage) 

    def total_amount_of_food(amount_of_food, amount_of_food_with_Xpercentage):
        total_amount_of_food = float(amount_of_food + amount_of_food_with_Xpercentage)
        return(total_amount_of_food) 

            