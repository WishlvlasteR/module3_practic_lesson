def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка корректности адресов
    if '@' not in sender or '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print('Невозможно отправить письмо самому себе!')
        return

    # Логика для стандартного и нестандартного отправителя
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'HЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Hello', 'wishiviaster99@gmail.com')
send_email('Hello', 'recipient@example.com', sender='university.heelp@gmail.com')
send_email('Hello', 'wishiviaster99gmail.com')
send_email('Hello', 'university.help@gmail.com')
