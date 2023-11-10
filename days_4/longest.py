def word_index(lst):
    count = -1
    for index, value in enumerate(lst):
        if len(value) > count:
            count = len(value)
            result_index = index
    if count > 0:
        return result_index
    else:
        return -1

words1 = ["Hate", "remorse", "vengeance"]
result_words1 = word_index(words1)
print(result_words1)