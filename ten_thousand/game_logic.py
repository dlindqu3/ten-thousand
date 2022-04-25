from random import randint
from collections import Counter

class GameLogic: 

  def __init__(self):
    pass 

  @staticmethod
  def calculate_score(tuple_of_ints): 
    score = 0
    num_counts = Counter(tuple_of_ints)
    if num_counts[1] == 1: 
      score += 100 
    elif num_counts[5] == 1: 
      score += 50 
    elif num_counts[1] == 3: 
      score += 1000
    elif num_counts



    #single 1: 100
    #single 5: 50
    #triple of num except 1: 100 x num 
    #triple 1: 1000
    #quadruple of num: (score for triple of num) * 2 
    #quintuple of num: (score for triple of num) * 3  
    #sextuple of num: (score for triple of num) * 4
    #sextuple of 1: 4000 == (score of triple for 1) * 4 
    #straight = 1500 

  @staticmethod
  def roll_dice(integer_length): 
    num_list = []
    for num in range(1, integer_length + 1):
      num_list.append(randint(1,6))
    return tuple(num_list)    

class Banker: 

  def __init__(self): 
    pass 

  def shelf(self, points): 
    pass 

  def bank(self):
    pass 

  def clear_shelf(self): 
    pass 
