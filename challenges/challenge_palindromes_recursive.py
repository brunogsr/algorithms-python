def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    elif high_index <= low_index:
        return True

    elif word[low_index] != word[high_index]:
        return False

    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
