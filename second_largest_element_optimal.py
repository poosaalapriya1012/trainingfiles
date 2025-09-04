def find_second_largest(arr):
    largest = arr[0]
    
    for num in arr[1:]:
        if num > largest:
            largest = num
    
    second_largest = float('-inf')  
    
    for num in arr:
        if num != largest and num > second_largest:
            second_largest = num
    
    return second_largest

arr = [1, 2, 7, 3, 4]
print("The second largest element in the array is:",find_second_largest(arr))
