"""
Created on Fri Dec 30 2022

@author: BigProgramme
         Saint Heraud MBOUMA
"""


class Nim:
    def __init__(self):
        self.tokens = 12
        self.player1 = input("Enter name of player 1 \n---> : ")
        self.player2 = input("Enter name of player 2 \n---> : ")
        self.tower = 1

    @staticmethod
    def rules():
        print("HERE ARE THE RULES OF THE GAME:")
        print("1- THIS GAME CONTAINS", 12, "TOKENS --->: ", 12 * " I ")
        print("2- THE GOAL IS TO TAKE BETWEEN 1 AND 3 TOKENS UNTIL THERE IS 0 TOKEN. BUT:")
        print("3- THE PLAYER WHO TAKES THE LAST TOKEN WILL BE THE LOSER.")
        print("GOOD LUCK!!!")
        return "\n"

    def get_token(self):
        if self.tower % 2 == 0:
            print(f"HOW MANY TOKENS DO YOU WANT? {self.player2}---> : ")
        else:
            print(f"HOW MANY TOKENS DO YOU WANT? {self.player1}---> : ")

        token_take = int(input())
        if token_take < 1 or token_take > 3:
            print("THE NUMBER OF TOKENS TO BE TAKEN MUST BE BETWEEN 1 AND 3.")
            int(input("CHANGE NUMBER--->: "))
        else:
            self.tower += 1
            self.tokens = self.tokens - token_take
            print("HE'S STAYING:", self.tokens * " I ", "<---", self.tokens, "IN THE GAME")

            if self.tower % 2 == 0:
                return f"{self.player1} YOU HAVE TAKEN : {token_take} TOKENS"
            else:
                return f"{self.player2} YOU HAVE TAKEN : {token_take} TOKENS"

    def next_tour(self):
        again = 0
        while self.tokens > 0:
            again = self.get_token()
        return again

    def winner(self):
        if self.tokens <= 0 and self.tower % 2 == 0:
            print("END OF THE GAME", self.player1, "YOU HAVE LOST")
            return f"THE WINNER IS :  {self.player2}..."

        if self.tokens <= 0:
            print("END OF THE GAME", self.player2, "YOU HAVE LOST")
            return f"THE WINNER IS:  {self.player1}..."


game = Nim()
print(game.rules())
print(game.get_token())
print(game.next_tour())
print(game.winner())
