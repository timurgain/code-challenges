def read_input() -> tuple:
    total_rows = int(input())
    total_columns = int(input())
    matrix = []
    row_number = 0
    while row_number < total_rows:
        matrix.append(list(map(int, input().strip().split())))
        row_number += 1
    search_row = int(input())
    search_column = int(input())
    return total_rows, total_columns, matrix, search_row, search_column

def func(total_rows, total_columns, matrix, search_row, search_column):    
    result = []
    if search_row != 0:
        neighbour_upstairs = matrix[search_row-1][search_column]
        result.append(neighbour_upstairs)
    if search_row != total_rows - 1:
        neighbour_bottom = matrix[search_row+1][search_column]
        result.append(neighbour_bottom)
    if search_column != 0:
        neighbour_left = matrix[search_row][search_column-1]
        result.append(neighbour_left)
    if search_column != total_columns - 1:
        neighbour_right = matrix[search_row][search_column+1]
        result.append(neighbour_right)
    result.sort()
    return ' '.join(map(str, result))

if __name__ == '__main__':
    total_rows, total_columns, matrix, search_row, search_column = read_input()
    y = func(total_rows, total_columns, matrix, search_row, search_column)
    print(y)
