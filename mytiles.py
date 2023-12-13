from enum import Enum

# možnosti hran dílků
class Edge(Enum):
    EMPTY = 0
    CITY = 1
    GRASS = 2
    PATH = 3

# rozměry obrázků, které používám
imgSizeY = 130
imgSizeX = 130

# názvy souborů s dílky a jejich hrany po směru hodinových ručiček
# první hodnota je sever, druhá západ, atd.
tilesDict = {
    "obrazky/obr0.jpg" : [Edge.CITY, Edge.CITY, Edge.CITY, Edge.CITY], 
    "obrazky/obr1.jpg" : [Edge.CITY, Edge.GRASS, Edge.CITY, Edge.CITY],
    "obrazky/obr2.jpg" : [Edge.CITY, Edge.PATH, Edge.CITY, Edge.CITY],
    "obrazky/obr3.jpg" : [Edge.CITY, Edge.GRASS, Edge.GRASS, Edge.CITY],
    "obrazky/obr4.jpg" : [Edge.CITY, Edge.PATH, Edge.PATH, Edge.CITY],
    "obrazky/obr5.jpg" : [Edge.CITY, Edge.GRASS, Edge.CITY, Edge.GRASS],
    "obrazky/obr6.jpg" : [Edge.CITY, Edge.GRASS, Edge.GRASS, Edge.GRASS],
    "obrazky/obr7.jpg" : [Edge.CITY, Edge.PATH, Edge.PATH, Edge.GRASS],
    "obrazky/obr8.jpg" : [Edge.CITY, Edge.PATH, Edge.GRASS, Edge.PATH],
    "obrazky/obr9.jpg" : [Edge.CITY, Edge.GRASS, Edge.PATH, Edge.PATH],
    "obrazky/obr10.jpg" : [Edge.CITY, Edge.PATH, Edge.PATH, Edge.PATH],
    "obrazky/obr11.jpg" : [Edge.GRASS, Edge.GRASS, Edge.GRASS, Edge.GRASS],
    "obrazky/obr12.jpg" : [Edge.GRASS, Edge.PATH, Edge.GRASS, Edge.GRASS], 
    "obrazky/obr13.jpg" : [Edge.GRASS, Edge.PATH, Edge.PATH, Edge.GRASS],
    "obrazky/obr14.jpg" : [Edge.GRASS, Edge.PATH, Edge.GRASS, Edge.PATH],
    "obrazky/obr15.jpg" : [Edge.GRASS, Edge.PATH, Edge.PATH, Edge.PATH],
    "obrazky/obr16.jpg" : [Edge.PATH, Edge.PATH, Edge.PATH, Edge.PATH]
}

# pomocná funkce pro nalezení obrázku k dílku a jeho rotace
def pictureTile(orientedTiles) :
    pictureToTile = dict()
    for key, value in tilesDict.items() :
        for rotation in range(0, 4) :
            newTile = value[rotation:] + value[:rotation]
            if newTile in orientedTiles and str(newTile) not in pictureToTile.items() :
                pictureToTile.update({str(newTile) : (key, rotation)})
    return pictureToTile

# funkce vrací true, pokud jsou dílky first a second kompatibilní
# to jest pokud mají stejný typ hran nebo nemají jednoznačně určenou hranu (hrana je Edge.EMPTY)
def compareTiles(first, second) :
    return (first[0] == second[0] or first[0] == Edge.EMPTY or second[0] == Edge.EMPTY) \
        and (first[1] == second[1] or first[1] == Edge.EMPTY or second[1] == Edge.EMPTY) \
        and (first[2] == second[2] or first[2] == Edge.EMPTY or second[2] == Edge.EMPTY) \
        and (first[3] == second[3] or first[3] == Edge.EMPTY or second[3] == Edge.EMPTY)