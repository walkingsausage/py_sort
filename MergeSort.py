
def merge(left_list, right_list):
    new_list = []
    left_index = 0
    right_index = 0
    left_length = len(left_list)
    right_length = len(right_list)

    while left_index < left_length and right_index < right_length:
        if left_list[left_index] < right_list[right_index]:
            new_list.append(left_list[left_index])
            left_index += 1
        else:
            new_list.append(right_list[right_index])
            right_index += 1

    if left_index == len(left_list):

        while right_index < right_length:
            new_list.append(right_list[right_index])
            right_index += 1
    else:
        while left_index < left_length:
            new_list.append(left_list[left_index])
            left_index += 1
    return new_list

def merge_sort(list_to_sort):
    """

    :rtype : object
    """
    if len(list_to_sort) <= 1:
        return list_to_sort

    mid_point = len(list_to_sort) / 2
    left_list = []
    right_list = []
    index = 0
    while index < mid_point:
        left_list.append(list_to_sort[index])
        index += 1
    while index < len(list_to_sort):
        right_list.append(list_to_sort[index])
        index += 1
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)



