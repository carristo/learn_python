def hello_user():
    while True:
        try:
            print('Скажи что-нибудь')
            msg = input()
            if msg.lower() == 'пока':
                print('Ну пока')
                break
            print(f'Сам ты {msg}')
        except KeyboardInterrupt:
            print('Ну пока')
            break


hello_user()
