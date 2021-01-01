def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    greater = []
    lower = []
    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item) 
    return quick_sort(lower) + [pivot] + quick_sort(greater)

print(quick_sort([2,3,1,7,5,10,8]))

#based on https://www.youtube.com/watch?v=kFeXwkgnQ9U
#used for study purposes
