someList = [5, 8, 6, 11, 2]
anotherList = [3,3]
def twoSum(num_list, target):
    target_value = 0
    while target_value != target:
        for i in range(0, len(num_list)-1):
            for j in range(i+1, len(num_list)):
                target_value = num_list[i] + num_list[j]
                if target_value == target:
                    new_list = [num_list.index(num_list[i]), num_list.index(num_list[j], i+1, len(num_list))]
                    return new_list
                else:
                    pass

print(twoSum(someList, 10))
print(twoSum(anotherList, 6))