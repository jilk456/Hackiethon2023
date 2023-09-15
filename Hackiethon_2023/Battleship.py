import random

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    def Search():
        print("searching")
        
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