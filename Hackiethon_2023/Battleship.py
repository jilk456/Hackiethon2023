import random

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    def Search():
        print("searching")
        highestX = 0
        highestY = 0
        highestProb = 0
        for x in range(10):
            for y in range(10):
                if ((x%2 == 0)and(y%2==0)) or ((x%2!=0) and (y%2!=0)):
                    if (probabilityGrid[x][y] > highestProb) and (map[x][y] == 0):
                        highestX = x
                        highestY = y
                        highestProb = highestProb
        return [highestX, highestY]

        
    def Hunt():
        print("hunting")
        x = p1ShotSeq[-1][0]
        y = p1ShotSeq[-1][1]
        print(str([x,y]) + " this is the hunt call")
        for i in range(4):
            if i == 0:
                if (x + 1) < 10 and storage[x + 1][y] == 0:
                    x += 1
                    break 
            elif i == 1:
                if (x - 1) > -1 and storage[x - 1][y] == 0:
                    x -= 1
                    break 
            elif i == 2:
                if (y + 1) < 10 and storage[x][y + 1] == 0:
                    y += 1
                    break 
            elif i == 3:
                if (y - 1) > -1 and storage[x][y - 1] == 0:
                    y -= 1
                    break 
            else:
                Search()

#Position refers to the coordinates of the top left
    def checkIfFits(shiplength, direction, positionX, positionY):
        if direction == "alongX":
            requiredPositions = [[x+positionX,positionY] for x in range(shiplength)]
        else:
            requiredPositions = [[positionX,positionY+y] for y in range(shiplength)]
        for position in requiredPositions:
            if not((position[0] < 10) and (position[1] < 10) and (map[position[0]][position[1]]!=1)):
                return False
        return True
    
    # Takes [x, y] list as input and gives the number of ship positions that could be on it
    def makeProbabilityGrid():
        ships = [5, 3, 3, 2, 2]
        probabilityGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]]
        for x in range(10):
            for y in range(10):
                for shiplength in ships:
                    if checkIfFits(shiplength, "alongX", x, y):
                        for num in range(shiplength):
                            probabilityGrid[x+num][y]+=1
                    if checkIfFits(shiplength, "alongY", x, y):
                        for num in range(shiplength):
                            probabilityGrid[x][y+num]+=1
        return probabilityGrid
    
        #Generates a map if there isn't one yet. 1 = hit, -1 = miss, 0 = unchecked
    if not storage:
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]]
    else:
        map = storage

    probabilityGrid = makeProbabilityGrid()


    x = 5
    y = 5
    
    #CHOOSE WHAT ALGO
    if p1PrevHit == True:
        #CHECK IF LAST HIT HAS EMPTY ADJACENT SQUARES
        x = p1ShotSeq[-1][0]
        y = p1ShotSeq[-1][1]
        for i in range(4):
            if i == 0:
                if (x + 1) < 10 and storage[x + 1][y] == 0:
                    Hunt()
                    break 
            elif i == 1:
                if (x - 1) > -1 and storage[x - 1][y] == 0:
                    Hunt()
                    break 
            elif i == 2:
                if (y + 1) < 10 and storage[x][y + 1] == 0:
                    Hunt()
                    break 
            elif i == 3:
                if (y - 1) > -1 and storage[x][y - 1] == 0:
                    Hunt()
                    break 
            else:
                Search()
    else:
        Search()


    return [x,y], map


print(ShipLogic(1, 1, 15, 15, [[0,0],[5,2],[1,8],[9,4]], True, None))
