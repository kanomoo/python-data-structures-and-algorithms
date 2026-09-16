def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        last_index = n - 1 - i
        swap = 0
        for j in range(last_index):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap += 1
        print(i, arr, swap)

if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(my_list)