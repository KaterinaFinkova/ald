import numpy as np
import random
import cv2
import mytiles
import matplotlib.pyplot as plt

class Board :

    def __init__(self, sizeX, sizeY, tiles) :
        self.sizeX = sizeX
        self.sizeY = sizeY
        # seznam orientovaných dílků
        self.tiles = tiles
        # tabulka, kterou chci zaplnit
        # hodnoty x a y jsou obráceně než je zvyklé, aby bylo jednodušší vytvořit konečný obrázek
        # dílek (0, 0) je v levém hodním rohu
        self.boardTiles = [[[mytiles.Edge.EMPTY, mytiles.Edge.EMPTY, mytiles.Edge.EMPTY, mytiles.Edge.EMPTY] \
                            for x in range(0, self.sizeX)] for y in range(0, self.sizeY)]
        # tabulka, zda dílek byl již navšíven nebo nebyl
        self.state = state = [[False for x in range(0, self.sizeX)] for y in range(0, self.sizeY)]

    # metoda vrací seznam dílků, které lze umístit na na pozici (x, y)
    def possibleTiles(self, y, x) :
        # nejprve se podívám, jaké má dílek sousedy
        north = mytiles.Edge.EMPTY if y - 1 < 0 else self.boardTiles[y-1][x][2]
        west = mytiles.Edge.EMPTY if x - 1 < 0 else self.boardTiles[y][x-1][3]
        south = mytiles.Edge.EMPTY if y + 1 >= self.sizeY else self.boardTiles[y+1][x][0] 
        east = mytiles.Edge.EMPTY if x + 1 >= self.sizeX else self.boardTiles[y][x+1][1]

        # pomocí funkce compareTiles vracím vhodné dílky z listu tiles
        tileList = []
        for tile in self.tiles :
            if mytiles.compareTiles(tile, [north, west, south, east]) :
                tileList.append(tile)
        return tileList

    # metoda rozmístí dílky na desku
    # vrací true, pokud existují vhodné kombinace, jinak false
    # metoda funguje rekurzivně, vrací se pokud neexistuje vhodný dílek pro danou kompozici
    def waveCollapseFunctionRecurzive(self, animation = False) :
        # procházím postupně všechny dílky
        if self.queue == [] :
            return True

        [nextY, nextX] = self.queue[0]
        self.queue.remove([nextY, nextX])
        
        # přidám sousedy dílku do fronty
        if nextX + 1 != self.sizeX and self.state[nextY][nextX+1] == False :
            self.state[nextY][nextX+1] = True
            self.queue.append([nextY, nextX+1])
        if nextY + 1 != self.sizeY and self.state[nextY+1][nextX] == False :
            self.state[nextY+1][nextX] = True
            self.queue.append([nextY+1, nextX])
        if nextX != 0 and self.state[nextY][nextX-1] == False :
            self.state[nextY][nextX-1] = True
            self.queue.append([nextY, nextX-1])
        if nextY != 0 and self.state[nextY-1][nextX] == False :
            self.state[nextY-1][nextX] = True
            self.queue.append([nextY-1, nextX])

        # všechny dílky, které lze použít na místo (x, y)
        possibilities = self.possibleTiles(nextY, nextX)

        while len(possibilities) > 0 :
            # vyberu náhodně jednu z možných dílků
            randomTile = possibilities[random.randrange(len(possibilities))] 
            possibilities.remove(randomTile)
            self.boardTiles[nextY][nextX] = randomTile

            if animation :
                self.animate()

            if self.waveCollapseFunctionRecurzive(animation) :
                return True

        # len(possibilities) == 0
        # nebyl nalezen vhodný dílek, vracím se...
        self.queue.insert(0, [nextY, nextX])
        self.boardTiles[nextY][nextX] = [mytiles.Edge.EMPTY, mytiles.Edge.EMPTY, mytiles.Edge.EMPTY, mytiles.Edge.EMPTY]
        return False

    # metoda zaplní tabulku dílky
    # parametr animation určuje, zda se bude zobrazovat průběh algoritmu
    def waveCollapseFunction(self, animation = False) :
        if animation :
            plt.ion()

        # kde algoritmus začne se vybere náhodně
        y = random.randrange(self.sizeY)
        x = random.randrange(self.sizeX)

        self.queue = [[y, x]]
        
        self.state[y][x] = True
        if self.waveCollapseFunctionRecurzive(animation) :
            print("Algoritmus uspesne ukoncen")
        else :
            print("Neni mozne vyplnit plochu")

    # metoda poskládá z obrázků jednotlivých dílků celou plochu
    def drawPicture(self) :
        pictureToTile = mytiles.pictureTile(self.tiles)
        finalImg = np.zeros((self.sizeY*mytiles.imgSizeY, self.sizeX*mytiles.imgSizeX, 3))
        for y in range(self.sizeY) :
            for x in range(self.sizeX) :
                tile = self.boardTiles[y][x]
                
                if str(tile) in pictureToTile.keys() :
                    [filename, rotation] = pictureToTile[str(tile)]

                    img = cv2.imread(filename)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                    if rotation == 1 :
                        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                    elif rotation == 2 :
                        img = cv2.rotate(img, cv2.ROTATE_180)
                    elif rotation == 3 :
                        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

                    finalImg[y*mytiles.imgSizeY:(y+1)*mytiles.imgSizeY, x*mytiles.imgSizeX:(x+1)*mytiles.imgSizeX, :] = img[:, :, :]/255
        return finalImg

    # metoda zobrazí animaci
    def animate(self) :
        img = self.drawPicture()
        plt.imshow(img)
        plt.draw()
        plt.pause(0.00001)
        plt.clf()

    # metoda zobrazí výsledek
    def showResult(self) :
        plt.ioff()
        img = self.drawPicture()
        plt.imshow(img)
        plt.show()