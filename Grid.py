grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def heart(list):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i],end=' ')
        print('')

    for i in range(len(grid[0])-1,-1,-1):
        for j in range(len(grid)):
            print(grid[j][i],end=' ')
        print('')

print(heart(grid))
