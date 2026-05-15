import math
import numpy as np

A = np.zeros((1,1))
B = np.zeros((1,1))

def subtract_rows(A, pivot_row_index, pivot_column_index):
    test_A = A
    pivot_val = test_A[pivot_row_index][pivot_column_index]
    pivot_row = test_A[pivot_row_index][:]
    L_column = np.zeros((A.shape[0], 1))
    L_column[pivot_row_index][0] = 1
    for row_index, rows in enumerate(test_A[pivot_row_index+1:, :]):
        row_index += pivot_row_index + 1
        row_val = rows[pivot_column_index]
        multiplier = row_val/pivot_val
        L_column[row_index][0] = multiplier
        temp_rows = pivot_row * multiplier
        new_row = rows - temp_rows

        test_A[row_index, :] = new_row
    return test_A, L_column

def reformat_rows(A):
    # this is ass and needs to be reworked but it works for the cases I can think of
    row = 0
    column = 0
    A_temp = A.copy()
    A_cols = [A[:, i].tolist() for i in range(A.shape[1])]
    pivot_locations = []
    L_columns = []

    while column < len(A_cols)-1:
        cache = [x for x in A_cols[column][row+1:]]
        non_zero_cache = [x+row+1 for x, y in enumerate(cache) if y != 0]
        pivot = A_temp[row][column]
        print(' ')
        print('New Row')
        print(A_temp)
        print('Column: ' + str(column) + ' Row: ' + str(row))
        print('cache: ' + str(cache))
        print('non-zero-cache: ' + str(non_zero_cache))
        print('pivot: ' + str(pivot))
        if non_zero_cache == [] and pivot == 0:
            # pivot is not present in column, must progress to next column
            column += 1
            pivot_locations.append(0)
        elif non_zero_cache == [] and pivot != 0:
            # pivot is @ row, column --> no need to subtract
            pivot_locations.append(row)
            row += 1
            column += 1
        elif non_zero_cache != [] and pivot == 0:
            # pivot is below row, column
            A_temp[[row, non_zero_cache[0]]] = A_temp[[non_zero_cache[0], row]]
        elif non_zero_cache != [] and pivot != 0:
            # pivot is @ row, column --> must subtract
            pivot_locations.append(row)
            A_temp, L_col = subtract_rows(A_temp, row, column)
            L_columns.append(L_col)
            row += 1
            column += 1

        A_cols = [A_temp[:, i].tolist() for i in range(A_temp.shape[1])]

    L_final = np.zeros((A.shape[0], 1))
    L_final[-1:][0] = 1
    L_columns.append(L_final)
    L = np.hstack(L_columns)
    print('L:')
    print(L)
    return A_temp, pivot_locations, L
        
            
def check_solveable():
    t = 1
    if A.shape[0] != B.shape[0]:
        print("Not solveable")
        t = 0
    else:
        for i in range(A.shape[0]):
            if A[i][i] == 0:
                print("Not solveable")
                return False
            elif np.sum(A) == 0:
                return 1
    return t==1

def __init__(a, b):
    A = a
    B = b
    reformat_rows(A)




# __init__(np.array([[1, 2, 3,9], [4,5,6,2], [1,7,8,9]]), np.array([[7], [8], [9]]))
input = np.array([[2, 1, -1, 3, 2],
              [4, 3, -2, 5, 1],
              [-2, 0, 3, -1, 4],
              [6, 5, -1, 8, 3]], dtype=float)
__init__(input, np.array([[7], [8], [9]]))