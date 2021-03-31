#!/usr/bin/env python
from utils import utils
class dog_food:
    number_small_dogs   = 0
    number_medium_dogs  = 0
    number_large_dogs   = 0 
    total_number_of_dogs = 0
    amount_of_food_small_dog = 0
    amount_of_food_for_all_dogs = 0
    total_amount_of_food = 0
    left_over_food = 0
    actual_amount_of_food = 0


number_small_dogs    = int(input("Enter number of small dogs :" ))
number_medium_dogs   = int(input("Enter number of medium dogs :" ))
number_large_dogs    = int(input("Enter number of large dogs :" ))
left_over_food       =  float(input("Enter any left over food :" )) 

total_number_of_dogs = utils.total_dog(int(number_small_dogs),int(number_medium_dogs),int(number_large_dogs))
print("Total number of all dogs", total_number_of_dogs)

amount_of_food_small_dog =  utils.amount_of_food_small_dog(number_small_dogs)
print("Amount of food for the small dogs is {} lbs ".format(amount_of_food_small_dog))

amount_of_food_medium_dog =  utils.amount_of_food_medium_dog(number_medium_dogs)
print("Amount of food  for the medium dogs is {} lbs ".format(amount_of_food_medium_dog))

amount_of_food_large_dog =  utils.amount_of_food_large_dog(number_large_dogs)
print("Amount of food for the large dogs is {} lbs ".format(amount_of_food_large_dog))

amount_of_food_for_all_dogs = utils.amount_of_food(amount_of_food_small_dog, amount_of_food_medium_dog, amount_of_food_large_dog)
print("Amount of food for all dogs is {} lbs ".format(amount_of_food_for_all_dogs)) 

amount_of_food_with_Xpercentage = utils.amount_of_food_with_Xpercentage(amount_of_food_for_all_dogs)
print("Amount of food for all dogs with x percent is {} lbs ".format(amount_of_food_with_Xpercentage)) 

total_amount_of_food = utils.total_amount_of_food(amount_of_food_for_all_dogs, amount_of_food_with_Xpercentage)
print("Total amount of food for all dogs with x percent is {} lbs ".format(total_amount_of_food)) 

actual_amount_of_food = total_amount_of_food - left_over_food
print("Total amount of food for all dogs with x percent is {} lbs ".format(actual_amount_of_food))


