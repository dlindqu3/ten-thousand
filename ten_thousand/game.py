from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker

class Game: 
  total_dice = 6
  round_num = 1
  new_game = Banker()
  playing = True
  kept_dice = ()
  def play(self, roller=GameLogic.roll_dice):
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    response = input('> ')
    if response == "n": 
      print('OK. Maybe another time')
    elif response == 'y': 
      while self.playing:
        print(f'Starting round {self.round_num}')
        print('Rolling 6 dice...')
        roll = roller(6)
        dice_roll = "*** "
        for num in roll:
          dice_roll += f"{str(num)} "
        dice_roll += "***"
        print(dice_roll)
        print('Enter dice to keep, or (q)uit:')
        res2 = input('> ')
        if res2 == 'q':
          print(f'Thanks for playing. You earned {self.new_game.balance} points')
          self.playing == False
          break
        elif res2 != 'q':
          int_kept = int(res2)
          x = [int(a) for a in str(int_kept)]
          self.total_dice -= len(x)
          score = GameLogic.calculate_score(x)
          # print(f"{score}")
          Banker.shelf(self.new_game, score)
          # print(self.new_game.shelved)
          print(f"You have {score} unbanked points and {self.total_dice} dice remaining")
          print("(r)oll again, (b)ank your points or (q)uit:")
          res3 = input('> ')
          if res3 == 'b':
            Banker.bank(self.new_game)
            print(f"You banked {score} points in round {self.round_num}")
            print(f"Total score is {self.new_game.balance} points")
            self.round_num += 1
            self.total_dice = 6
          elif res3 == 'q':
            self.playing = False

if __name__ == "__main__":
    game = Game()
    game.play()
