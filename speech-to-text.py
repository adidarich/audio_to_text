import whisper


def speech_recognize(model='base'):
    # передаем load_model вызванную у whisper в переменную
    speech_model = whisper.load_model(model)

    # transcribe передаем звуковой объект
    result = speech_model.transcribe('/music.mp3')

    # save result in file
    with open(f'transcription_{model}.txt', 'w') as file:
        # в result мы получим огромный словарь с данными, нас в нем интересует ключ text
        file.write(result['text'])


def main():
    # создаем словарь, ключами будут цифры, значениями название модели
    # доступные модели tiny, base, small, medium, large
    models = {
        '1': 'tiny',
        '2': 'base',
        '3': 'small',
        '4': 'medium',
        '5': 'large'
    }

    # пробегаем циклам по словарю
    for k, v in models.items():
        print(f'{k}, {v}')

    # просим у пользователя ввести цифру, для того чтобы какую модель он хочет использовать
    user_model = int(input('Select a model by passing a number from 1 to 5: '))

    # проверка значении
    if user_model not in models.keys():
        raise KeyError(f"Models {models} not listed")

    print('The [транскрибация] started, please wait...')
    speech_recognize(model=models[user_model])


if __name__ == '__main__':
    main()
