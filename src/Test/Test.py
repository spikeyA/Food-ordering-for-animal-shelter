#!/bin/env python
import unittest
from   Animal-Shelter-Food-Ordering-System.Food-ordering-for-animal-shelter.src.onfig  import config 
from ..src.utils import utils
from ..src.main import dog_food

#Testcase 1 : Total number of dogs is less than 30.
def check_total_number_of_dogs(self):
    self.assertLessEqual(30,dog_food.total_amount_of_food())
    



