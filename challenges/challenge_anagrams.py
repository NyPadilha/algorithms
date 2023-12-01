def is_anagram(first_string, second_string):
    first_string = ''.join(merge_sort(first_string.lower()))
    second_string = ''.join(merge_sort(second_string.lower()))

    return first_string, second_string, first_string == second_string


def merge_sort(letters):
    if len(letters) <= 1:
        return letters

    mid = len(letters) // 2
    left = merge_sort(letters[:mid])
    right = merge_sort(letters[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


print(is_anagram("William Shakespeare", "I am a weakish speller"))
