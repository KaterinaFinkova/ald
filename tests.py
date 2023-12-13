import numpy as np
import random
import cv2
import mytiles
import board
import matplotlib.pyplot as plt
from enum import Enum

# TEST 1

# vygeneruji všechny možné orientace dílku
# první hodnota bude sever dílku, druhá západ, třetí jih, čtvrtá sever
orientedTiles = []
for key, value in mytiles.tilesDict.items() :
    for i in range(0, 4) :
        newTile = value[i:] + value[:i]
        if newTile not in orientedTiles :
            orientedTiles.append(newTile)

board1 = board.Board(20, 16, orientedTiles)
# metoda waveCollapse se nebude nikdy vracet, protože použiji všechny dílky a všechny jejich možné rotace 
board1.waveCollapseFunction()
# zobrazí výsledek
board1.showResult()


# TEST 2

# tyto dlaždice by měli odpovídat ukázce ze zadání - tedy metoda waveCollapseFunction se bude vracet
orientedTiles = [
    [mytiles.Edge.PATH, mytiles.Edge.PATH, mytiles.Edge.PATH, mytiles.Edge.PATH],
    [mytiles.Edge.GRASS, mytiles.Edge.GRASS, mytiles.Edge.GRASS, mytiles.Edge.PATH],
    [mytiles.Edge.PATH, mytiles.Edge.GRASS, mytiles.Edge.GRASS, mytiles.Edge.PATH],
    [mytiles.Edge.PATH, mytiles.Edge.PATH, mytiles.Edge.GRASS, mytiles.Edge.GRASS],
    [mytiles.Edge.GRASS, mytiles.Edge.PATH, mytiles.Edge.PATH, mytiles.Edge.GRASS],
]

board2 = board.Board(10, 10, orientedTiles)
board2.waveCollapseFunction(True) # animace je zapnutá, může trvat dlouho než doběhne
board2.showResult()

# TEST 3

# tímto dílkem nelze vyplnit plochu
orientedTiles = [[mytiles.Edge.GRASS, mytiles.Edge.GRASS, mytiles.Edge.GRASS, mytiles.Edge.PATH]]
board3 = board.Board(10, 10, orientedTiles)
board3.waveCollapseFunction()