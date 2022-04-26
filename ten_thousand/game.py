from ten_thousand.game_logic import GameLogic

class Game: 
  def play(self, roller=GameLogic.roll_dice):
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    response = input('> ')
    if response == "n": 
      print('OK. Maybe another time')
    elif response == 'y': 
      print('Starting round 1')
      #later - make number of dice dynamic 
      print('Rolling 6 dice...')
      # print('***  4 4 5 2 3 1 ***') # for one and done
      print('*** 4 2 6 4 6 5 ***') # for bank one roll then quit 
      print('Enter dice to keep, or (q)uit:')
      res2 = input('> ')
      if res2 == 'q':
        print('Thanks for playing. You earned 0 points')
      elif res2 != 'q':
        score = GameLogic.calculate_score((res2))
        print(f"You have {score} unbanked points and 5 dice left")


# Enter dice to keep, or (q)uit:
# > 5
# You have 50 unbanked points and 5 dice remaining
# (r)oll again, (b)ank your points or (q)uit:
# > b
# You banked 50 points in round 1
# Total score is 50 points
# Starting round 2
# Rolling 6 dice...
# *** 6 4 5 2 3 1 ***
# Enter dice to keep, or (q)uit:
# > q
# Thanks for playing. You earned 50 points