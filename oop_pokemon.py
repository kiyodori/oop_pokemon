# oop_pokemon.py
from game import Game
from pokemon import Pikachu, Hitokage

pikachu = Pikachu()
hitokage = Hitokage()
game = Game(pikachu, hitokage)
game.battle()
