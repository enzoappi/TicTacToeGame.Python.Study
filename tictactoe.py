import time
import os
import random


class Board:
    def __init__(self):
        self.player = {1: "X", 2: "O"}
        self.areas={1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

    def get_player(self, n):
        return self.player[n]

    def set_areas(self, n, player):
        self.areas[n] = player

    def get_areas(self, n):
        return self.areas.get(n)

    def play_choices(self, player):
        players_play_choice = None
        while players_play_choice not in (1, 9):
            try:               
                players_play_choice = int(input(f"Player '{self.get_player(player)}' what's your play: "))
                if self.get_areas(players_play_choice) == self.get_player(player) or self.get_areas(players_play_choice) != " ":
                        print("\nThis Area has already been chosen! Please select another one.\n")
                        players_play_choice = None
                else:
                        self.set_areas(players_play_choice, self.get_player(player))
                        break
            except Exception as e:
                tipo_erro = type(e).__name__
                print(f"\nERROR: {tipo_erro}!\nPlease type a valid option.\n")    
        self.show_map(True)
        if not self.test_victory(): 
            self.play_choices(2 if player == 1 else 1)
    
    def test_victory(self):
        victory_sequencies = [
            (1, 2, 3), (1, 4, 7), (1, 5, 9), 
            (2, 5, 8), (3, 6, 9), (3, 5, 7), 
            (4, 5, 6), (7, 8, 9)
        ]
        for vs in victory_sequencies:
            if self.areas[vs[0]] == self.areas[vs[1]] == self.areas[vs[2]] != " ":
                print(f"\nCongrats player '{self.areas[vs[0]]}'! You've won the match with the sequence {vs}!\n")
                return True
        if all(v != " " for v in self.areas.values()):
            print("\nWe've a draw match.\n")
            return True
        else:
            return False

    def show_map(self, bulean):
        print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print(f"{'CHOOSE YOUR AREA NUMBER'.center(37)}")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n")

        print("       |       |       ")
        print(f"  {self.areas.get(1) if bulean else 1}    |   {self.areas.get(2) if bulean else 2}   |   {self.areas.get(3) if bulean else 3}   ")
        print("       |       |       ")
        print("-------|-------|-------")
        print("       |       |       ")
        print(f"  {self.areas.get(4) if bulean else 4}    |   {self.areas.get(5) if bulean else 5}   |   {self.areas.get(6) if bulean else 6}   ")
        print("       |       |       ")
        print("-------|-------|-------")
        print("       |       |       ")
        print(f"  {self.areas.get(7) if bulean else 7}    |   {self.areas.get(8) if bulean else 8}   |   {self.areas.get(9) if bulean else 9}   ")
        print("       |       |       ")

        print("\n")

def main():
    while True:
        board = Board()
        board.show_map(False)
        board.play_choices(1)
        try:
            r = int(input("""
            Type: 
            
                0 - Continue
                          
                        OR
                          
                1 - Exit
            
            type you choice: """))
            if r == 1:
                print("\nSee you later! Thanks for playing Tic Tac Toe's Game!\n")
                break
        except Exception as e:
            tipo_erro = type(e).__name__
            print(f"\nERROR: {tipo_erro}!\nPlease type a valid option.\n")

#Play-time
main()