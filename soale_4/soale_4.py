# Transpose a Matrix:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'matrix: {matrix}')
print('')
list1=[]
list2=[]
# Transpose the matrix
for i in zip(*matrix):
    list(i)
    list1.append(list(i))
print(f'Transpose matrix in list: {list1}')
print('')

for i in zip(*matrix):
    list2.append(i)
print(list2)



