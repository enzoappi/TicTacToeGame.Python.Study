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

    def set_areas(self, n, symbol):
        self.areas[n] = symbol

    def get_areas(self, n):
        return self.areas.get(n)

    def play_choices(self):
        players_play_choice = None
        computers_play_choice = None
        while True:
            while players_play_choice not in (1, 9):
                try:               
                    players_play_choice = int(input("What's your play: "))
                    if self.get_areas(players_play_choice) == self.player or self.get_areas(players_play_choice) not in (" "):
                            print("This Area has already been chosen! Please select another one.")
                            players_play_choice = None
                    else:
                            self.set_areas(players_play_choice, self.player)
                            break
                except Exception as e:
                    tipo_erro = type(e).__name__
                    print(f"\nERROR: {tipo_erro}!\nPlease type a valid option.\n")    
            self.show_actual_play()
            if self.test_victory()==True: break
            time.sleep(0.8)
            while True:
                computers_play_choice = random.randint(1, 9)
                if self.get_areas(computers_play_choice) == self.computer_player or self.get_areas(computers_play_choice) != " ":
                    computers_play_choice = random.randint(1, 9)
                else:
                    self.set_areas(computers_play_choice, self.computer_player)
                    break
            self.show_actual_play()
            if self.test_victory()==True: break

    def test_victory(self):
        victory_sequencies = [
            (1, 2, 3), (1, 4, 7), (1, 5, 9), 
            (2, 5, 8), (3, 6, 9), (3, 5, 7), 
            (4, 5, 6), (7, 8, 9)
        ]
        for vs in victory_sequencies:
            if self.areas[vs[0]] == self.areas[vs[1]] == self.areas[vs[2]] != " ":
                print(f"Congrats player '{self.areas[vs[0]]}'! You've won the match with the sequence {vs}!")
                return True
                #return self.areas[vs[0]], vs
        if all(v != " " for v in self.areas.values()):
            print("We've a draw match.")
            return True
        else:
            return False

    def show_actual_play(self):
        print("\n")
        print("       |       |       ")
        print(f"  {self.areas.get(1)}    |   {self.areas.get(2)}   |   {self.areas.get(3)}   ")
        print("       |       |       ")
        print("-------|-------|-------")
        print("       |       |       ")
        print(f"  {self.areas.get(4)}    |   {self.areas.get(5)}   |   {self.areas.get(6)}   ")
        print("       |       |       ")
        print("-------|-------|-------")
        print("       |       |       ")
        print(f"  {self.areas.get(7)}    |   {self.areas.get(8)}   |   {self.areas.get(9)}   ")
        print("       |       |       ")

    def show_map(self):
        print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print(f"{'CHOOSE YOUR AREA NUMBER'.center(37)}")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n")

        print("       |       |       ")
        print(f"  {1}    |   {2}   |   {3}   ")
        print("       |       |       ")
        print("-------|-------|-------")
        print("       |       |       ")
        print(f"  {4}    |   {5}   |   {6}   ")
        print("       |       |       ")
        print("-------|-------|-------")
        print("       |       |       ")
        print(f"  {7}    |   {8}   |   {9}   ")
        print("       |       |       ")

        print("\n")

def main():
    board = Board()
    board.show_map()
    #time.sleep(1)
    #os.system('cls')
    board.set_players_type()
    board.play_choices()

#Play-time
main()