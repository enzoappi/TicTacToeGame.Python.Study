import time
import os
import random


class Board:
    def __init__(self):
        self.player = None
        self.computer_player = None
        self.areas={1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

    def set_players_type(self):
        r = None
        while r not in(1, 2):
            try:
                r = int(input("""
                Which kind of player you want to be? 
                
                1 - X
               
                2 - O
               
                type you choice: """))
            except Exception as e:
                tipo_erro = type(e).__name__
                print(f"\nERROR: {tipo_erro}!\nPlease type a valid option.\n")
        self.player = "X" if r==1 else "O"
        self.computer_player = "O" if r==1 else "X"

    def set_areas(self, n, player):
        self.areas[n] = player

    def get_areas(self, n):
        return self.areas.get(n)

    def play_choices(self):
        while True:
            players_play_choice = None
            computers_play_choice = None
            while players_play_choice not in (1, 9):
                try:               
                    players_play_choice = int(input("What's your play: "))
                    if self.get_areas(players_play_choice) == self.player or self.get_areas(players_play_choice) != " ":
                            print("\nThis Area has already been chosen! Please select another one.\n")
                            players_play_choice = None
                    else:
                            self.set_areas(players_play_choice, self.player)
                            break
                except Exception as e:
                    tipo_erro = type(e).__name__
                    print(f"\nERROR: {tipo_erro}!\nPlease type a valid option.\n")    
            self.show_map(True)
            if self.test_victory(): break
            time.sleep(0.8)
            while True:
                computers_play_choice = random.randint(1, 9)
                if self.get_areas(computers_play_choice) == self.computer_player or self.get_areas(computers_play_choice) != " ":
                    computers_play_choice = random.randint(1, 9)
                else:
                    self.set_areas(computers_play_choice, self.computer_player)
                    break
            self.show_map(True)
            if self.test_victory(): break

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
    board = Board()
    board.show_map(False)
    board.set_players_type()
    board.play_choices()

#Play-time
main()