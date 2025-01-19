# Разбираем пример сортировки

def findSmallest(arr):

    smallest = arr[0]

    smallest_index = 0

    for i in range(1, len(arr)):

        if arr[i] < smallest:

            smallest = arr[i]

            smallest_index = i

    return smallest_index


# Сортировка с нахождением наименьшего индекса

def selectionSort(arr):

    newArr = []

    copiedArr = list(arr)

    for i in range(len(copiedArr)):

        smallest = findSmallest(copiedArr)

        newArr.append(copiedArr.pop(smallest))

    return newArr
