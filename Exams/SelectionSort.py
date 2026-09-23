def selection_sort(arr):
    n = len(arr)
    print("Original:       ", arr, "min_idx swap")
    for i in range(n):
        swap = 0
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: min_idx = j

        if min_idx != i:
            swap += 1
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
        print(f"For i = {i}, j = {j} {arr} {min_idx:4} {swap:5}")
    print(f"Result : {str(arr)}")

if __name__ == "__main__":
    my_list = [64, 25, 12, 22, 11]
    selection_sort(my_list)
