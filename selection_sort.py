test_list = [32, 0, 4, 5, -8, 10, 2, -21, 3, -33, 100, -5]
test_list2 = [112, 17, -84, -8, 10, -2, -4, 3, -33, 200, 65]

def selection_sort(some_list):
    x = 0
    while x < len(some_list):
        min_value = minimum(some_list[x:len(some_list)])
        index_min_value = some_list.index(min_value)
        if min_value < some_list[x]:
            some_list[index_min_value], some_list[x] = some_list[x], some_list[index_min_value]
        else:
             some_list[x], some_list[index_min_value] = some_list[index_min_value], some_list[x]
        print(some_list)
        x += 1
    return some_list

def minimum(some_list):
    x = 0
    min_value = some_list[x]
    while x <= len(some_list) - 1:
        if min_value > some_list[x]:
            min_value = some_list[x]
        else:
            min_value = min_value
        x += 1
    return min_value

print(selection_sort(test_list))
print(selection_sort(test_list2))