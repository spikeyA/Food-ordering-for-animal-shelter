#!/bin/env python
import unittest
from config import config 
from utils import utils
from main import dog_food


class Testfoodordering(unittest.TestCase):
   
    #Testcase 1 : Total number of dogs is less than 30.
    def check_total_number_of_dogs():
        assertLessEqual(dog_food.total_amount_of_food, 30)  
        

    #Testcase 2 : Total number of dogs is equal to 0.
    def check_zero_dogs():
        assertEqual(dog_food.total_amount_of_food, 0)  
        

    #Testcase 3 : Total number of dogs is more than 30.
    def check_more_than30_dogs():
        assertGreaterEqual(verify_numberdog_food.total_amount_of_food, 30)  

    #Testcase 4 : Is left_over_food  accepts fraction value.
    def check_value_float():
        assertIsInstance(dog_food.left_over_food, float)   


if __name__ == '__main__':
    
    Testfoodordering.check_total_number_of_dogs()
    Testfoodordering.check_zero_dogs()
    Testfoodordering.check_more_than30_dogs()
    Testfoodordering.check_value_float()

    print("All test passed")
  