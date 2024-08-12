import time
import os
import random


class Board:
    def __init__(self):
        self.areas={1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

    def set_areas(self, n, symbol):
        self.areas[n] = symbol

    def get_areas(self, n):
        return self.areas.get(n)

    def players_play_choice(self, player_symbol, pc_symbol):
        play_choice = 9999999
        pc_play_choice = 9999999
        while play_choice not in (1, 9):
           try:
               
               play_choice = int(input("What's your play: "))
               if self.get_areas(play_choice) == player_symbol or self.get_areas(play_choice) not in (" "):
                    print("This Area has already been chosen! Please select another one.")
                    play_choice = 9999999
               else:
                    self.set_areas(play_choice, player_symbol)
                    break
           except Exception as e:
            tipo_erro = type(e).__name__
            print(f"\nERROR: {tipo_erro}!\nPlease type a valid option.\n")
                
        self.show_actual_play()
        time.sleep(0.8)
        while True:
            pc_play_choice = random.randint(1, 9)
            if self.get_areas(pc_play_choice) == pc_symbol or self.get_areas(pc_play_choice) not in (" "):
                pc_play_choice = random.randint(1, 9)
            else:
                self.set_areas(pc_play_choice, pc_symbol)
                break
        self.show_actual_play()

    def test_victory(self):
        pass

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

class Player:
    def __init__(self):
        self.player_name = 'Anonymus'
        self.player_type = "none"
        self.pc_player_type = "none"

    def set_player_name(self):
        self.player_name = input("Type your name, player: ")

    def get_player_name(self):
        return self.player_name

    def set_player_type(self):
        r = 9999999
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
        self.player_type = "X" if r==1 else "O"
        self.set_pc_player_type()

    def get_player_type(self):
        return self.player_type

    def set_pc_player_type(self):
        if self.player_type == "X":
            self.pc_player_type="O"
        elif self.player_type == "O":
            self.pc_player_type="X"

    def get_pc_player_type(self):
        return self.pc_player_type


#main
##player = Player()
##board = Board()
##player.set_player_name()
##player.set_player_type()
#print(f"{player.get_player_name()}: {player.get_player_type()}")
#print(f"Computer: {player.get_pc_player_type()}")
##board.show_map()
##time.sleep(1)
##os.system('cls')
##board.show_actual_play()
##while True:
##    board.players_play_choice(player.get_player_type(), player.get_pc_player_type())
##print("GAME OVER!")

meu_dict = {1: "X", 2: "O", 3: "X", 4: "O", 5: "X", 6: "O", 7: "O", 8: " ", 9: "X"}
dicionario_inverso = {}
for chave, valor in meu_dict.items():
    #print(f"chave: {chave}")
    #print(f"valor: {valor}")
    if valor not in dicionario_inverso:
        print(f"\nchave (IF): {chave}")
        print(f"valor (IF): {valor}")
        dicionario_inverso[valor] = [chave]
        print(f"dicionario_inverso (IF): {dicionario_inverso}")
    else:
        print(f"\nvalor (ELSE): {valor}")
        dicionario_inverso[valor].append(chave)
        print(f"dicionario_inverso (ELSE): {dicionario_inverso}")

# Exibindo chaves com valores iguais
for valor, chaves in dicionario_inverso.items():
    if len(chaves) > 1:
        print(f'Valor {valor} encontrado nas chaves: {chaves}')