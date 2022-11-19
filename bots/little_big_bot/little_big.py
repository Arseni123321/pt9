number = 100
count_of_attempts = 1

while True:
    try:
        answer = int(input('Введи число: '))

        if answer == number:
            print('Ты гений')
            print(f'Количесво попыток: {count_of_attempts}')

            with open('high_score.txt', 'w+') as high_score:
                if len(high_score.read()) == 0:
                    high_score.write(f'{count_of_attempts}')
                    break
                elif int(high_score.read()) > count_of_attempts:
                    print('Ты установил рекорд :|')
                    high_score.write(f'{count_of_attempts}')
                    break
        elif number < answer:
            print('Меньше')
            count_of_attempts += 16
        else:
            print('Больше')

    except ValueError:
        print(f'\n[ERROR] Данные должны иметь числовой тип')