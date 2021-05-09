def sudoku2(grid):
    grid_size = len(grid)
    for i in range(grid_size):
        repeated_number = set()
        check_columns = set()
        for j in range(grid_size):
            if grid[i][j].isnumeric():
                if grid[i][j] not in repeated_number:
                    repeated_number.add(grid[i][j])
                else:
                    return False
            if grid[j][i].isnumeric():
                if grid[j][i] not in check_columns:
                    check_columns.add(grid[j][i])
                else:
                    return False
    
    # For 3x3 window
    for i in range(1, len(grid), 3):
        for j in range(1, len(grid), 3):
            box_number_isrepeated = set()
            for element in (grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], \
                            grid[i][j-1], grid[i][j], grid[i][j+1], \
                            grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1] ):
                if element.isnumeric() and element not in box_number_isrepeated:
                    box_number_isrepeated.add(element)
                elif element.isnumeric() and element in box_number_isrepeated:
                    return False

    return True