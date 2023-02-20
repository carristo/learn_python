names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name: str):
    current_name = names.pop()
    while True:
        print(current_name)
        if current_name == name:
            print(f'{name} нашёлся!')
            break
        if len(names) == 0:
            print(f'{name} не найден :(')
            break
        current_name = names.pop()

find_person('Даша')