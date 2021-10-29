test_list = [32, 0, 4, 5, -8, 10, 2, -21, 3, 33, 100, -5, 1, 6, -13]
test_list2 = [112, 17, -84, -8, 10, -2, -4, 3, -33, 200, 65, 76, -23]

def insertion_sort(some_list):
    x = 0
    while x < len(some_list):
        min_value = minimum(some_list[x:len(some_list)])
        some_list.remove(min_value)
        some_list.insert(x, min_value)
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

print(insertion_sort(test_list))
print(insertion_sort(test_list2))