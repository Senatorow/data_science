"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    global limit_1 # зададим плавающие границы поиска
    limit_1 = 1
    global limit_2
    limit_2 = 101
    
    
    while True:
        count += 1
        predict_number = (limit_2 + limit_1) // 2 # предполагаемое число  - среднее между двух границ
        if number > predict_number: # если загаданное больше предполагаемого, то...
            limit_1 = predict_number # ...нижняя граница смещается до значения предполагаемого
        if number < predict_number: # если загаданное меньше, то...
            limit_2 = predict_number # ...верхняя граница смещается до значения предполагаемого
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

    
# RUN
if __name__ == "__main__":
    score_game(random_predict)
