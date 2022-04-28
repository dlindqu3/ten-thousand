from random import randint
from collections import Counter

class GameLogic: 

  def __init__(self):
    pass 

  @staticmethod
  def get_scorers(roll):
    if roll == ():
      return roll
    roll_count = Counter(roll)
    for num in roll_count:
      return_list = []
      score = GameLogic.calculate_score(roll)
      if score == 1500:
        return roll
      if roll_count[1] > 0:
        for num in range(1, roll_count[1]+1):
          return_list.append(1)
      if roll_count[5] > 0:
        for num in range(1, roll_count[5]+1):
          return_list.append(5)
      if roll_count[num] > 3:
        return_list.append(num)
      return tuple(return_list)

  def filter_response(roll, input):
    for num in roll:
      if roll[num] < input[num]: 
        return 'BAD' 
      
      

  def validate_keepers(roll, response, filter_response = filter_response):
    dice_list_check = [int(num) for num in response]
    input_counts = Counter(dice_list_check)
    roll_counts = Counter(roll)
    cheat_check = filter_response(roll_counts, input_counts)
    if cheat_check:
      return False
    else:
      return True


  @staticmethod
  def calculate_score(tuple_of_ints): 
    score = 0
    num_counts = Counter(tuple_of_ints)
    pairs = []
    three_of_kind = []

    if num_counts[1] and num_counts[2] and num_counts[3] and num_counts[4] and num_counts[5] and num_counts[6]:
      score = 1500
      return score 
    for num in num_counts:
      if num_counts[num] == 2:
        pairs.append(num)
    if len(pairs) == 3:
      score += 1500
      return score
    for num in num_counts:
      if num_counts[num] == 3:
        three_of_kind.append(num)
    if len(three_of_kind) == 2:
      score += 1200
      return score
    if num_counts[1] == 1 and num_counts[5] == 1:
      score += 150
    elif num_counts[1] == 1: 
      score += 100 
    elif num_counts[1] == 2:
      score += 200
    elif num_counts[1] == 3:
      score += 1000
    elif num_counts[1] == 4:
      score += 2000
    elif num_counts[1] == 5:
      score += 3000
    elif num_counts[1] == 6:
      score += 4000
    
    if num_counts[5] == 1 and num_counts[1] != 1: 
      score += 50 
    elif num_counts[5] == 2:
      score += 100

    for num in num_counts:
      if num_counts[1] != 3 and num_counts[1] != 4 and num_counts[1] != 5 and num_counts[1] != 6:
        if num_counts[num] >= 3:
          if num_counts[num] == 6:
            score += num * 400
          elif num_counts[num] == 5:
            score += num * 300
          elif num_counts[num] == 4:
            score += num * 200
          elif num_counts[num] == 3:
            score += num * 100

    return score

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
