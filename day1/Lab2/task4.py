def bubble_sort(list):
    n = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if list[i-1] > list[i]:
                list[i-1], list[i] = list[i], list[i-1]
                swapped = True
        n -= 1
    return list


print("Input [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] -> ",
      bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

print("Input [1, 2, 3, 4, 5] -> ",
      bubble_sort([1, 2, 3, 4, 5]))

print("Input [5, 4, 3, 2, 1] -> ",
      bubble_sort([5, 4, 3, 2, 1]))
