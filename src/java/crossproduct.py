import pandas as pd
matrix =[[2,7,6],[8,9,2], [3,8,6]]

def determinant(matrix):
    patrix = pd.DataFrame(matrix)
    a = patrix.iloc[0,0]* patrix.iloc[1,1]
    b = patrix.iloc[0,1]* patrix.iloc[1,0]
    return a-b
    