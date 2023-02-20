names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

current_name = names.pop()
while True:
    print(current_name)
    if(current_name == 'Валера'):
        print('Валера нашёлся!')
        break
    current_name = names.pop()
