from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys

class Game: 
  def __init__(self, max_rounds=20):
    self.total_dice = 6
    self.round_num = 1
    self.banker = Banker()
    self.playing = True
    self.kept_dice = ()
    self.max_rounds = max_rounds 

  def play(self, roller=GameLogic.roll_dice):
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    response = input('> ')
    if response == "n": 
      print('OK. Maybe another time')
    elif response == 'y': 
        self.manage_rounds(roller)


  def format_dice_roll(self, roll):
        dice_roll = "*** "
        for num in roll:
          dice_roll += f"{str(num)} "
        dice_roll += "***"
        return dice_roll

  def manage_rounds(self, roller):
      if self.max_rounds == self.round_num:
        print(f'Thanks for playing. You earned {self.banker.balance} points') 
        sys.exit()

      print(f'Starting round {self.round_num}')
      while self.playing:
        print(f'Rolling {self.total_dice} dice...')
        roll = roller(self.total_dice)
        formatted_roll = self.format_dice_roll(roll)
        print(formatted_roll)
        zilch_list = [int(num) for num in roll]
        zilch_check = GameLogic.calculate_score(zilch_list)
        if zilch_check == 0:
          self.banker.clear_shelf()
          print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
          print(f"You banked {self.banker.shelved} points in round {self.round_num}")
          print(f"Total score is {self.banker.balance} points")
          self.round_num += 1
          self.total_dice = 6
          self.manage_rounds(roller)
        else:
          cheat_check = False
          while not cheat_check:
            print('Enter dice to keep, or (q)uit:')
            res2 = input('> ')
            if res2 != 'q':
                cheat_check = GameLogic.validate_keepers(roll, res2)
                if not cheat_check: 
                  print("Cheater!!! Or possibly made a typo...")
                  print(formatted_roll)

            if res2 == 'q':
              self.playing = False
              print(f'Thanks for playing. You earned {self.banker.balance} points')
              break
          if res2 != 'q':
            # res2 = res2.split(' ')
            # res2 = ''.join(res2)
            dice_list = [int(num) for num in res2]
            self.total_dice -= len(dice_list)
            score = GameLogic.calculate_score(dice_list)
            self.banker.shelf(score)
            print(f"You have {self.banker.shelved} unbanked points and {self.total_dice} dice remaining")
            if self.total_dice == 0:
              self.total_dice = 6
            print("(r)oll again, (b)ank your points or (q)uit:")
            res3 = input('> ')
            if res3 == 'b':
              print(f"You banked {self.banker.shelved} points in round {self.round_num}")
              self.banker.bank()
              print(f"Total score is {self.banker.balance} points")
              self.round_num += 1
              self.total_dice = 6
              self.manage_rounds(roller)
            elif res3 == 'q':
              self.playing = False
              print(f'Thanks for playing. You earned {self.banker.balance} points')
              break



if __name__ == "__main__":
    game = Game()
    game.play()

