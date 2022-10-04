
import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

print(len(twoDArray))

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0 )
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))


def access_elements(array, rowindex, colindex):
    if rowindex >= len(array) or colindex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowindex][colindex])


access_elements(newTwoDArray, 3, 1)


def traverse_2darray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverse_2darray(twoDArray)


def search_2darray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element not found'


print(search_2darray(twoDArray, 444))

newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)
