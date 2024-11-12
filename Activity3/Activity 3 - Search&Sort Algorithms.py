"""This program explores sorting and search algorithms in a set of phases that are all interconnected. The objective is to create, sort, extend, and search for items within an array. Additionally, we use this practical method to identify which sorting and search algorithms are suitable for different situations."""

import random
import time
from array import array

# PHASE 1 - INSERTION SORT 

def generate_sorted_data(data):
    """This function uses insertion sort to organize a set of random integers from least to greatest."""

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# PHASE 2 - RECURSIVE BINARY SEARCH

def binary_search(sorted_array, target, left=0, right=None):
    """This function performs binary search on a sorted array to find the target value."""

    if right == None:
        right = len(sorted_array) - 1
    if left > right:
        return None
    midpoint = (left + right) // 2
    if sorted_array[midpoint] > target:
        return binary_search(sorted_array, target, left, midpoint - 1)
    elif sorted_array[midpoint] < target:
        return binary_search(sorted_array, target, midpoint + 1, right)
    else:
        return midpoint

# PHASE 3 - RECURSIVE MERGE SORT - Shahid Bora

def merge_sort(data):
    """This function uses merge sort to sort the integers in a large array from least to greatest."""

    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])
    sorted_list = array('i')
    i = 0 
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1
    for k in range(i, len(left_half)):
        sorted_list.append(left_half[k])
    for k in range(j, len(right_half)):
        sorted_list.append(right_half[k])
    return sorted_list

def generate_large_sorted_data(size, old_arr, old_arr_len):
    """This function is reponsible for extending the original array into one that is larger."""

    large_data = old_arr + array('i', [random.randint(1, 1000) for i in range(size - old_arr_len)])
    return large_data

def sort_large_data(ext_arr):
    """This function assigns a variable to the large, sorted array in order to allow us to call it. (PROBABLY NOT PRODUCTIVE BUT IT WORKS)"""

    sorted_data_large = merge_sort(ext_arr)
    return sorted_data_large

# PHASE 4 - SEARCH PERFORMANCE COMPARISON - Mohammed Arsalan

def linearsearch(targetinput, arrayinput):
    """This function performs linear search on a sorted array to find a target value."""
    
    for index in range(len(arrayinput)):
        if arrayinput[index] == targetinput:
            return index
    return None

def linearvsbinary(targetvalue, sorteddata):
    """This function compares between linear and binary search by allowing us to know which one is faster."""

    linearstart = time.perf_counter()
    if linearsearch(targetvalue, sorteddata) != None:
        print(f"Object {targetvalue} found at index {linearsearch(targetvalue, sorteddata)} in the sorted array using linear search.")
    else:
        print(f"Object {targetvalue} not found in the sorted array.")
    linearstop = time.perf_counter()
    binarystart = time.perf_counter()
    if binary_search(sorteddata, targetvalue) != None:
        print(f"Object {targetvalue} found at index {binary_search(sorteddata, targetvalue)} in the sorted array using binary search.")
    else:
        print(f"Object {targetvalue} not found in the sorted array.")
    binarystop = time.perf_counter()
    lineartime = f"{linearstop - linearstart:.6f}"
    binarytime = f"{binarystop - binarystart:.6f}"
    print(" ")
    print(f"It took Linear Search {lineartime} seconds to find the target")
    print(f"It took binary search {binarytime} seconds to find the target")
    print(" ")
    if lineartime > binarytime:
        print("Binary Search took less time and was faster.")
    elif binarytime == lineartime:
        print("Both Binary Search and Linear Search took the same amount of time to find the Target")
    else:
        print("Linear Search took less time and was faster.")
    print("--------------------------")



def main():
    size = random.randint(5, 15)
    unsorted_data = array('i', [random.randint(1, 100) for i in range(size)])
    sorted_data = generate_sorted_data(unsorted_data[:])

    print("PHASE 1 - Initiating Insertion Sort... ")
    print("--------------------------")
    print(f"Array before insertion sort algorithm: {unsorted_data}")
    print(f"Array after insertion sort algorithm: {sorted_data}")
    print("Insertion Sort complete.")
    print("--------------------------")
    print("")

    print("PHASE 2 - Initiating Binary Search... ")
    print("--------------------------")
    target = int(input("Type your target value: "))
    print(f"Searching for target value: {target}")

    if binary_search(sorted_data, target) != None:
        print(f"Object {target} found at index {binary_search(sorted_data, target)} in the sorted array.")
    else:
        print(f"Object {target} not found in the sorted array.")
    print("Binary Search complete.")
    print("--------------------------")
    print("")

    print("PHASE 3 - Sorting Larger data set with merge sort...")
    print("--------------------------")
    Extension = int(input("How many elements do you want? "))
    while Extension <= size:
        print("Size extension is too small/equal to current length")
        Extension = int(input("How many elements do you want?: "))
    large_unsorted_data = generate_large_sorted_data(Extension, unsorted_data, size)
    print("")
    print(f"Extended array before sort: {large_unsorted_data}\n")
    large_sorted_data = sort_large_data(large_unsorted_data)
    print(f"Extended array after sort: {large_sorted_data}")
    print("--------------------------")
    print("")

    print("PHASE 4 - Using binary and linear search on extended array...")
    print("--------------------------")
    searchvalue = int(input("Input a number to search using linear and binary Search: "))
    print("")

    linearvsbinary(searchvalue, large_sorted_data)



if __name__ == "__main__":
    main()



# REFLECTION QUESTION

# QUESTION
"""How does the choice of sorting algorithm impact the performance of searching algorithms? Discuss why binary search is faster than linear search on large,sorted data and how efficient sorting methods enhance overall performance."""

# ANSWER
"""The choice of sorting algorithm affects search efficiency since sorted data enables faster searching. Binary search is faster than linear search on large, sorted datasets because it repeatedly divides the dataset in half to find an item, whereas linear search checks each items one-by-one. Efficient sorting methods, such as merge sort or insertion sort, prepare data by arranging it in order, allowing searches like binary search to be performed much faster than if the data were unsorted, which improves overall performance in data retrieval tasks."""

