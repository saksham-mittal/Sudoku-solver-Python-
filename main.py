def writeAns(arr):
    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            f.write("-------|-------|-------\n")
        for j in range(0, 9):
            if j % 3 == 0 and j != 0:
                f.write(" |")
            f.write(" %d" % arr[i][j])
        f.write("\n")
    f.write("\n\n")

def check(grid, grid_number, id):
    line_number = grid_number // 9
    column_number = grid_number % 9
    for x in grid[line_number]:
        if x == id:
            return False

    for x in range(0, 9):
        if grid[x][column_number] == id:
            return False

    box_i = line_number - line_number % 3
    box_j = column_number - column_number % 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[box_i + i][box_j + j] == id:
                return False

    return True

def solver(grid, grid_number):

    if grid[grid_number // 9][grid_number % 9] == 0:
        digits = [x for x in range(1, 10)]
        for test_no in digits:
            if check(grid, grid_number, test_no) == True:
                grid[grid_number // 9][grid_number % 9] = test_no
                # writeAns(test)           # In case you want to write the steps of solving
                if grid_number == 80:
                    return True
                if(solver(grid, grid_number + 1) == True):
                    return True
                else:
                    grid[grid_number // 9][grid_number % 9] = 0
    else:
        if(solver(grid, grid_number + 1) == True):
            return True

    return False

f = open("solved.txt", "w+")
ftestcase = open("testcase.txt", "r")

test = []
for line in ftestcase:
    test.append([int(x) for x in line.split()])

ftestcase.close()

if solver(test, 0) == True:
    writeAns(test)
else:
    f.write("The sudoku cannot be solved!")

f.close()
