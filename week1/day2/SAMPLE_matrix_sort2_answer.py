
<<<<<<< HEAD
# from tabulate import tabulate
=======
from tabulate import tabulate
>>>>>>> 69b0729... updated git repo

def matrix_sort(matrix_doc):
    with open(matrix_doc, 'r') as f:
        document = f.readlines()
    #return document


    matrix = []
    for row in document:
        matrix.append(list(map(int, row.split())))
    #return matrix

#ROW SUMS:

    row_sums=[]
    for row in matrix:
        row_sums.append(sum(row))
    #return row_sums
    print ("Row Sums: ", row_sums)
#COLUMN SUMS

    column_sums=[]
    for a in range (len(matrix[1])):
        i = 0
        for r in range (len(matrix)):
            i+=matrix[r][a]
        column_sums.append(i)
    #return column_sums
    print ("Column sums: ", column_sums)
    #return "Row Sums: ", row_sums, "Column Sums: ", column_sums

#ROW SORTED MATRIX:

    enumerated_rows=list(enumerate(row_sums))
    enumerated_rows=sorted(enumerated_rows, key=lambda x: x[1])
    #return enumerated_rows


    sorted_by_row=[]
    for i in range(len(row_sums)):
        sorted_by_row.append(matrix[enumerated_rows[i][0]])
    #return sorted_by_row

#COLUMN SORTED MATRIX:

    enumerated_columns=list(enumerate(column_sums))
    enumerated_columns=sorted(enumerated_columns, key=lambda x: x[1])
    #return enumerated_columns


    sorted_by_column=[[]for i in range(len(matrix))]
    for i in range(len(enumerated_columns)):
        for j in range(len(matrix)):
            sorted_by_column[j].append(matrix[j][enumerated_columns[i][0]])
    #return sorted_by_column

    print ("Sorted by row: ")
<<<<<<< HEAD
    print ((sorted_by_row))
=======
    print (tabulate(sorted_by_row))
>>>>>>> 69b0729... updated git repo
    #for i in sorted_by_row:
        #print (i)

    print ("\n\n")

    print ("Sorted by column: ")
    print (tabulate(sorted_by_column))
    #for i in sorted_by_column:
        #print (i)



matrix_sort("testmatrix.txt")
