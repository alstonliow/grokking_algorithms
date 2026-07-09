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

print(quicksort([10, 5, 5, 3, 7, 6, 1, 4, 9, 8]))
print(quicksort([2]))       # one element   
print(quicksort([2, 1]))    # two elements
print(quicksort([]))        # empty list