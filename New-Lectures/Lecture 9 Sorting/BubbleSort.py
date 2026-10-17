def bubble_sort(arr):
    n = len(arr)
    print(f"Original,  arr = {arr}")
    for i in range(n):
        last_index = n - 1 - i
        swap = 0
        for j in range(last_index):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap += 1
                print(f"Swap {temp} and {arr[j]}")
        print(f"For loop i = {i} arr = {arr}")
    print(f"Result :     {arr}")

if __name__ == "__main__":
    my_list = [5, 1, 4, 2, 8]
    bubble_sort(my_list)