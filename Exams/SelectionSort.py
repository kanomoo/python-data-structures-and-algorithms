def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: min_idx = j

        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
        print(i, arr, j)

if __name__ == "__main__":
    my_list = [64, 51, 34, 32, 21, 8]
    selection_sort(my_list)
