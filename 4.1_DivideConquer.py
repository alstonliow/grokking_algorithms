#sum(for)

def sum_for(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum_for([1, 2, 3, 4, 5]))

#sum_D&C(recursion) #ex4.1
#sum function using recursion

def sum_dc(arr):
    if len(arr) == 0:
        return 0 
    else:
        return arr[0] + sum_dc(arr[1:])
    
print(sum_dc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#ex4.2 #num_elements_D&C(recursion)
#calculate number of element in a list using recursion

def num_elements(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + num_elements(arr[1:])
    
print(num_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#ex4.3 Max(recursion)
#find largest number in a  
#

def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        return arr[0] if arr[0] > find_max(arr[1:]) else find_max(arr[1:])

print(find_max([1, 2, 3, 4, 5, 6, 7, 8, 90, 10]))
