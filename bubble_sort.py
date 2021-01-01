def bubble_sort(arr):
    length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, length):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

#based on https://www.youtube.com/watch?v=g_xesqdQqvA
#used for study purposes