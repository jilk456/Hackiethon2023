import random
from re import X, search

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    def Search(map):
        print("searching")
        probabilityGrid = makeProbabilityGrid()
        highestX = 0
        highestY = 0
        highestProb = 0
        for i in range(10):
            print(probabilityGrid[i])
        for x in range(10):
            for y in range(10):
                if ((x%2 == 0)and(y%2==0)) or ((x%2!=0) and (y%2!=0)):
                    if (probabilityGrid[x][y] > highestProb) and (map[x][y] == 0):
                        highestX = x
                        highestY = y
                        highestProb = probabilityGrid[x][y]
        print("Highest probability =",highestProb)
        return [highestX, highestY]

        
    def Hunt(xPos, yPos):
        #print("hunting")
        searchfind = False
        for i in range(4):
            if i == 0:
                if ((xPos + 1) < 10) and (storage[xPos + 1][yPos]) == 0:
                    xPos += 1
                    searchfind = True
                    continue
            elif i == 1:
                if (xPos - 1) > -1 and storage[xPos - 1][yPos] == 0:
                    xPos -= 1
                    searchfind = True
                    continue
            elif i == 2:
                if (yPos + 1) < 10 and storage[xPos][yPos + 1] == 0:
                    yPos += 1
                    searchfind = True
                    continue 
            elif i == 3:
                if (yPos - 1) > -1 and storage[xPos][yPos - 1] == 0:
                    yPos -= 1
                    searchfind = True
                    continue 

        print(searchfind)
        if searchfind == True:
            return [xPos, yPos]
        else:
            return "womp womp"


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


    #If not first move, sends info of whether last move was a hit to map
    if p1ShotSeq:
        xPrev = p1ShotSeq[-1][0] - 1
        yPrev = p1ShotSeq[-1][1] - 1

        if p1PrevHit:
            map[xPrev][yPrev] = 1
        else:
            map[xPrev][yPrev] = -1
    
#CHOOSE ALGORITHM
    hitsList = []
    huntingFind = False
    for xlist in range(len(map)):
        for ylist in range(len(map[xlist])):
            if map[xlist][ylist] == 1:
                hitsList.append([xlist, ylist])
    print(hitsList)

    for i in range(len(hitsList)):
        test = Hunt(hitsList[i][0],hitsList[i][1])
        if test != "womp womp":
            x = test[0]
            y = test[1]
            huntingFind = True
            #print([x, y])
            continue
    if huntingFind == False:
        searchResult = Search(map)
        x = searchResult[0]
        y = searchResult[1]
        #print([x, y])
    



    return [x + 1, y + 1], map
