import readchar
import os

player={
    "x":0,
    "y":0
}

tiles={
    0:"🟦",
    1:"🟩",
    2:"🔴"
}

def newMap(w,h):
    return [[0 for x in range(w)] for y in range(h)]

mapWidth=9
mapHeight=8
map=newMap(mapWidth,mapHeight)

def draw(grid):
    os.system("clear")

    map=newMap(mapHeight,mapWidth)

    map[mapHeight][0]=1

    while player["y"]<mapHeight-1:
        player["y"]+=1

    map[player["y"]][player["x"]]=2

    for y in range(len(grid)):
        s=""
        for x in range(len(grid[y])):
            s+=tiles[map[y][x]]
        print(s)

draw(map)

while True:
    k=readchar.readkey()
    key=k.lower()

    if key=="a" and player["x"]>0:
        player["x"]-=1
        draw(map)
    elif key=="d" and player["x"]<mapWidth-1:
        player["x"]+=1
        draw(map)
        


    