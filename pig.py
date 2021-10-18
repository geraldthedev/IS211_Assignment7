import random


class DiceRoll:
    def __init__(self):
        self.__sides = 6
    pass

    def roll(self):
        roll_result = int(random.randint(1, self.__sides))
        
        return roll_result
pass 
 


class Player:
    def __init__(self, roll):
        
        self.score = 0
        self.roll = roll
        pass     


def game():
    
    
    score = 0
    goal = 100
    yes = True
    no = False
    again = True
    stay = False
    
    ready = input("Are you ready to play?")
    if ready is yes:
        roll = DiceRoll().roll()
        player=Player(roll)
        player_score = player.roll
        players = {
            "player1": player,
            "player2": player
    }
        while player_score <= goal:
            again= input("Roll again? Or stay? ")
            if again is again and goal <= 100:
                
                play_turn=+1
                new_roll = DiceRoll().roll()
                roll_again = player_score + new_roll
                player_score = roll_again
                added_score = player_score
                print(added_score)
                if new_roll is 1:
                    player_score = 0
                    print("Your score has been rest")
                    print(player_score)
            if again is stay:
                player_score = added_score
                players.get(player)
                print("the turn has ended. ")
        if ready is no:
            print("Maybe you will be ready to play next time.")
        pass   

        

if __name__ == "__main__":
    game()
    pass
    
