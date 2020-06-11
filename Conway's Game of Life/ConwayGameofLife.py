import numpy as np
import matplotlib.pyplot as plt



def randomConway(prba):
    return np.random.choice([0,1], 100*100, p=[1-prba,prba]).reshape(100,100)
def updateConway(grid):
    newConway = grid.copy()
    for i in range(100):
        for j in range(100):
            total = (grid[i, (j-1)%100] + grid[i, (j+1)%100] + 
                         grid[(i-1)%100, j] + grid[(i+1)%100, j] +
                         grid[(i-1)%100, (j-1)%100] + grid[(i-1)%100, (j+1)%100] +
                         grid[(i+1)%100, (j-1)%100] + grid[(i+1)%100, (j+1)%100])
            if grid[i, j] == 1:
                if(total <2) or (total > 3):
                    newConway[i, j] = 0
            else:
                if total == 3:
                    newConway[i, j] = 1
    global gridup 
    gridup = newConway
    
    grid[:] = newConway[:]
    return plt.imshow(newConway)

def conway(grid):
    grid = updateConway(grid)
    

def runConway(num, prba):
    for a in range(1):
        conway(randomConway(prba))
        plt.pause(.01) #update the figure here
    for b in range(num):
        conway(gridup)
        plt.pause(.01) #and here
        plt.clf()
    plt.close()