def insetion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        c = i - 1
        while c >= 0 and arr[c] > key:
            arr[c + 1] = arr[c]
            c = c - 1
            #print(arr)
        arr[c + 1] = key
    return arr

#based on: https://www.youtube.com/watch?v=S5no2qT8_xg
#used for study purposes
