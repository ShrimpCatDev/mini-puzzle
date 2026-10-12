import readchar
import os

player={
    "x":0,
    "y":0
}

tiles={
    0:"🟦",
    1:"🟩"
}

def newMap(w,h):
    return [[0 for x in range(w)] for y in range(h)]

map=newMap(9,8)

def draw(grid):
    os.system("clear")

    map=newMap(9,8)

    map[player["y"]][player["x"]]=1

    for y in range(len(grid)):
        s=""
        for x in range(len(grid[y])):
            s+=tiles[map[y][x]]
        print(s)

draw(map)

while True:
    k=readchar.readkey()
    key=k.lower()

    if key=="w":
        print("up")
        draw(map)


    