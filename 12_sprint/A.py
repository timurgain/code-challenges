"""Matrix transposition."""


def read_input() -> tuple:
    initial_rows = int(input())
    initial_columns = int(input())
    initial_matrix = []
    row_number = 0
    while row_number < initial_rows:
        initial_matrix.append(list(input().strip().split()))
        row_number += 1
    return initial_rows, initial_columns, initial_matrix


def func(initial_rows, initial_columns, initial_matrix):    
    transpos_matrix = [[] for i in range(0, initial_columns)]
    for new_column in range(0, initial_rows):
        for new_row in range(0, initial_columns):
            transpos_matrix[new_row].append(initial_matrix[new_column][new_row])
    return transpos_matrix


if __name__ == '__main__':
    initial_rows, initial_columns, initial_matrix = read_input()
    for i in func(initial_rows, initial_columns, initial_matrix):
        print(' '.join(i), end='\n')
