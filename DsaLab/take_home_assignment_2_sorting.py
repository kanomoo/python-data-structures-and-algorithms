"""
================================================================================
Data Structures & Algorithms - Take-Home Programming Assignment 2
Instructor: Dr. Pradit Pitaksatheinkul
Due Date: Sunday Midnight, 27 September 2026 (5 Points)
Topics: Implementation of Sorting Algorithms (Insertion, Selection, Bubble Sort)
        with Pass-by-Pass Tracing & Swap/Shift Counts.
================================================================================
"""

def insertion_sort(arr):
    """
    Insertion Sort Implementation matching Dr. Pradit's lecture specification.
    Builds the sorted array one item at a time by shifting elements and inserting.
    """
    a = arr.copy()
    n = len(a)
    total_shifts = 0
    print("=" * 65)
    print("--- INSERTION SORT TRACE ---")
    print(f"Original Array: {a}")
    print(f"Pass 0: {a} (Initial State)")
    
    for p in range(1, n):
        tmp = a[p]
        j = p
        shift_count = 0
        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
            shift_count += 1
        a[j] = tmp
        total_shifts += shift_count
        print(f"Pass {p}: Array={a} | Shifts this pass={shift_count}")
        
    print(f"Sorted Result: {a}")
    print(f"Total Shifts/Operations: {total_shifts}")
    print("=" * 65)
    return a


def selection_sort(arr):
    """
    Selection Sort Implementation matching Dr. Pradit's lecture specification.
    Finds the minimum element from the unsorted part and swaps it with the first element.
    """
    a = arr.copy()
    n = len(a)
    total_swaps = 0
    print("=" * 65)
    print("--- SELECTION SORT TRACE ---")
    print(f"Original Array: {a}")
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
                
        swapped = False
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            total_swaps += 1
            swapped = True
            
        unsorted_part = a[i+1:] if i + 1 < n else []
        print(f"Round {i + 1}: Min={a[i]} (found at idx {min_idx}) | Array={a} | Unsorted={unsorted_part} | Swapped={swapped}")
        
    print(f"Sorted Result: {a}")
    print(f"Total Swaps: {total_swaps}")
    print("=" * 65)
    return a


def bubble_sort(arr):
    """
    Bubble Sort Implementation matching Dr. Pradit's lecture specification.
    Repeatedly steps through the list, compares adjacent elements, and swaps them if out of order.
    """
    a = arr.copy()
    n = len(a)
    total_swaps = 0
    print("=" * 65)
    print("--- BUBBLE SORT TRACE ---")
    print(f"Original Array: {a}")
    
    for i in range(n - 1):
        last_index = n - 1 - i
        swap_this_pass = 0
        for j in range(last_index):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_this_pass += 1
        total_swaps += swap_this_pass
        print(f"Pass {i + 1}: Array={a} | Swaps this pass={swap_this_pass} | Largest '{a[last_index]}' placed at index {last_index}")
        
    print(f"Sorted Result: {a}")
    print(f"Total Swaps: {total_swaps}")
    print("=" * 65)
    return a


def main():
    print("=================================================================")
    print("   DATA STRUCTURES & ALGORITHMS - PROGRAMMING ASSIGNMENT 2       ")
    print("   Student Submission: Sorting Algorithms Verification           ")
    print("=================================================================\n")
    
    # Test Data 1 from Lecture Notes & Slides
    test_data_1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Test Dataset 1: {test_data_1}\n")
    bubble_sort(test_data_1)
    print()
    
    # Test Data 2 from Lecture Notes & Slides
    test_data_2 = [64, 25, 12, 22, 11]
    print(f"Test Dataset 2: {test_data_2}\n")
    selection_sort(test_data_2)
    print()
    
    # Test Data 3 from Lecture Notes & Slides
    test_data_3 = [34, 8, 64, 51, 32, 21]
    print(f"Test Dataset 3: {test_data_3}\n")
    insertion_sort(test_data_3)
    print()


if __name__ == "__main__":
    main()
