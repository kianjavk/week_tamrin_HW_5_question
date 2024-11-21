

import time
import random

def generate_random_list(size=1000):
    return [random.randint(0, 1000) for _ in range(1000)]
def test(a,b):
    c = a+b
    d = a-b
    return c,d
f,e= test(1,2)
f,_= test(1,2)
_,e= test(1,2)
# Bubble Sort
def bubble_sort(numbers_list):
    n = len(numbers_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
    return numbers_list

# Merge Sort
def mergeSort(num):
    if len(num) <= 1:
        return num

    mid = len(num) // 2
    leftHalf = mergeSort(num[:mid])
    rightHalf = mergeSort(num[mid:])
    return merge(leftHalf, rightHalf)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = quick(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

# Timing each sort
sizes = 1000
large_list = generate_random_list(sizes)

# Bubble Sort Timing
start_time = time.time()
sorted_list_bubble = bubble_sort(large_list.copy())
end_time = time.time()
bubble_sort_time = end_time - start_time
print(f"Bubble Sort Time: {bubble_sort_time:.10f} seconds")

# Merge Sort Timing
start_time = time.time()
sorted_list_merge = mergeSort(large_list.copy())
end_time = time.time()
merge_sort_time = end_time - start_time
print(f"Merge Sort Time: {merge_sort_time:.10f} seconds")

# Quick Sort Timing
start_time = time.time()
sorted_list_quick = quicksort(large_list.copy())
end_time = time.time()
quick_sort_time = end_time - start_time
print(f"Quick Sort Time: {quick_sort_time:.10f} seconds")

