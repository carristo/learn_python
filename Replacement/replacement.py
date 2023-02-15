def replace_first_8_symbols(initial_str : str) -> str:
    return f'autotest{initial_str[8:]}'


def replace_all_until_first_dash(initial_str : str) -> str:
    i = initial_str.find("-")
    return f'autotest{initial_str[i:]}'


print(replace_first_8_symbols("a1a1a1a1-a1a1-a1a1-a1a1a1a1a1a1"))
print(replace_all_until_first_dash("b1b1b1b1-b1b1-b1b1-b1b1b1b1b1b1"))
