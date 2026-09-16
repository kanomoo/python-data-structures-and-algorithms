def insertion_sort(a):
    total = 0
    print(0, a, None)
    for p in range(1, len(a)):
        tmp = a[p]
        j = p
        swap = 0
        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
            swap += 1
        a[j] = tmp
        total += swap
        print(p, a, swap)
    print(total)

if __name__ == "__main__":
    my_list = [34, 8, 64, 51, 32, 21]
    # my_list = [64, 51, 34, 32, 21, 8]

    insertion_sort(my_list)