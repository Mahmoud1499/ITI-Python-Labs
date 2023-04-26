def reduce_adjacent_elements(list):
    reduced_list = [list[0]]  
    for i in range(1, len(list)):
        if list[i] != list[i-1]:  
            reduced_list.append(list[i])  
    return reduced_list


print("input [1, 2, 3, 3] -> ", reduce_adjacent_elements([1, 2, 3, 3]))
print("input [1, 2, 2, 3, 3, 3]-> ",
      reduce_adjacent_elements([1, 2, 2, 3, 3, 3]))
print("input [1, 2, 2, 3, 3, 3]-> ",
      reduce_adjacent_elements([1, 2, 2, 3, 3, 3]))

