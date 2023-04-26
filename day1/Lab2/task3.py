def all_different(seq):
    return len(seq) == len(set(seq))


print("Input [1, 5, 7, 9] -> ", all_different([1, 5, 7, 9]))

print("input [2, 4, 5, 5, 7, 9] -> ", all_different([2, 4, 5, 5, 7, 9]))
