def binary_search(arr, target):
    minimun = 0
    maximun = len(arr) - 1

    while minimun <= maximun:
        '''
        while target was not found
        '''
        guess = maximun + minimun // 2

        if arr[guess] == target:    return guess
        elif arr[guess] < target:   minimun = guess + 1
        else:                       maximun = guess - 1

    return False

#based on https://www.youtube.com/watch?v=DnvWAd-RGhk&t=301s
#used for study purposes