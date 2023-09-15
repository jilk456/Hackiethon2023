import random
from re import search
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
        



    return [x,y], storage


print(ShipLogic(1, 1, 15, 15, [[0,0],[5,2],[1,8],[9,4]], True, None))