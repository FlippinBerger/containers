import random #used in quickSort

def swap(l, i1, i2):
    temp = l[i1]
    l[i1] = l[i2]
    l[i2] = temp

def bubbleSort(l):
    size = len(l)
    finished = False

    while not finished:
        finished = True
        for i in range(size):
            if i + 1 > size - 1:
                continue
            if l[i] > l[i+1]:
                finished = False
                swap(l, i, i + 1)


def insertionSort(l):
    for i in range(1, len(l)):
        temp = l[i]
        j = i
        while j > 0 and temp < l[j - 1]:
            l[j] = l[j - 1]
            j -= 1
        l[j] = temp


def selectionSort(l):
    for i in range(len(l)):
        small_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[small_index]:
                small_index = j
        swap(l, i, small_index)


def mergeSort(l):
    if len(l) > 1:
        mid = len(l) / 2
        left = l[:mid]
        right = l[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1

#quickSort base function
def quickSort(l):
    _quickSort(l, 0, len(l) - 1)


#quickSort helper function
def _quickSort(l, first, last):
    if first < last:
        pivot = partition(l, first, last)
        _quickSort(l, first, pivot - 1)
        _quickSort(l, pivot + 1, last)


#function to partition the list for quickSort
def partition(l, first, last):
    pivot = first + random.randrange(last - first + 1)
    swap(l, first, last)
    
    for i in range(first, last):
        if l[i] <= l[last]:
            swap(l, i, first)
            first += 1
    swap(l, first, last)
    return first

