def get_sum(one, two, delimiter = '&'):
    return f'{one}{delimiter}{two}'


result_string = get_sum('Learn', 'python')
print(result_string)
print(result_string.upper())