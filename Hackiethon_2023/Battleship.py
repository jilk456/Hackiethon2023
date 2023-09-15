import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit):
    x = random.randint(1,10)
    y = random.randint(1,10)
    return [x,y] 
    
    # Generating a map for the enemy
    def makeEnemyMap():
        for x in 10:
            for y in 10:
                enemyMap[x][y] = 0
    
