import numpy as np

movement_dict = {'r' : np.array([0, +1]),
                 'l' : np.array([0, -1]),
                 'u' : np.array([+1, 0]),
                 'd' : np.array([-1, 0]),
}

def gen_empty_grid(n):
    gridsize = int(np.ceil(np.sqrt(n)))
    if gridsize % 2 == 0:
        gridsize += 1
    grid = np.zeros([gridsize, gridsize]).astype(int)
    return grid

def to_0123(n):
    nr = n
    while nr > 3:
        nr -= 4
    return nr

def gen_instructions(grid):
    n = len(grid)
    move_order = 'rdlu'
    mult = 0
    moves = ""
    i = 0
    while len(moves) <= n**2:
        if i % 2 == 0:
            mult += 1            
        movement = move_order[to_0123(i)]
        moves += mult*movement
        i += 1
    moves = moves[0:n**2-1]
    return moves

def make_grid(n):
    grid = gen_empty_grid(n)
    instructions = gen_instructions(grid)
    n = len(grid)
    mid = (n-1)/2
    loc = np.array([mid, mid]).astype(int)
    grid[loc[0], loc[1]] = 1
    for i, move in enumerate(instructions):
        move = movement_dict[move]
        loc += move
        num = i + 2
        grid[loc[0], loc[1]] = num        
    return grid
    
def part1(n):
    grid = make_grid(n)
    mid = (len(grid)-1)/2
    mid_index = np.array([mid, mid])
    itemindex = np.where(grid==n)
    dist_vector = np.array(itemindex).flatten() - mid_index
    dist = np.sum(np.abs(dist_vector))
    return dist
    
if __name__ == "__main__":
    for i in range(100):
        result = part1(325489)
    print(result)
