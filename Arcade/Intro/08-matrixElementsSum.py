
def matrixElementsSum(matrix):
   rows = len(matrix)
   cols = len(matrix[0])
   sum = 0
   
   def sum_rows(col):
    sum_aux = 0
    for i in range(0,rows):
        if matrix[i][col] == 0:
            return sum_aux
        else:
            sum_aux += matrix[i][col]
    return sum_aux
    
   for j in range(cols):
       sum += sum_rows(j)
   
   return sum