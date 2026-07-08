def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = []
        larger = []
        for i in arr[1:]:
            if i <= pivot:
                smaller.append(i)
            else:
                larger.append(i)
        return quicksort(smaller) + [pivot] +quicksort(larger) #recursion #most important part of the code

print(quicksort([10, 5, 2, 3, 7, 6, 1, 4, 9, 8]))