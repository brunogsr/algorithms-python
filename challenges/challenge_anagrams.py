def sort_string(string):
    if len(string) <= 1:
        return ''.join(string)

    middle = len(string) // 2
    left_half = string[:middle]
    right_half = string[middle:]

    left_sorted = sort_string(left_half)
    right_sorted = sort_string(right_half)

    sorted_string = []
    i = j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            sorted_string.append(left_sorted[i])
            i += 1
        else:
            sorted_string.append(right_sorted[j])
            j += 1
    sorted_string.extend(left_sorted[i:])
    sorted_string.extend(right_sorted[j:])

    return ''.join(sorted_string)


print(sort_string("exemplo"))


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return (sort_string(list(first_string.lower())),
                sort_string(list(second_string.lower())), False)
    sorted_first = sort_string(list(first_string.lower()))
    sorted_second = sort_string(list(second_string.lower()))
    return (sorted_first, sorted_second,  sorted_first == sorted_second)


print(is_anagram('', ''))
