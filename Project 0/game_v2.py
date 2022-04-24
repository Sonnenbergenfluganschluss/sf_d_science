"""Игра угадай число.
Компьютер сам загадывает и угадывает число.
"""

import numpy as np

def predict_20(number: int = 1) -> int:
    """Угадываем число менее, чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # счётчик попыток
    
    # задаём начальные экстремумы диапазона поиска 
    min = 1
    max = 100
    
    while True:
        count += 1 
        predict_number = int(round(np.mean(range(min, max + 1)))) # предполагаемое число при каждой попытке - среднее между экстремумами
        if predict_number > number:
            max = predict_number
        if predict_number < number:
            min = predict_number
        if number == predict_number:
            break # если угадали число, - выходим из цикла
    return(count)


def score_game(random_predict):
    """Подсчёт среднего количества попыток угадывания за 1000 подходов 

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    # np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(30)) # можно, конечно и 1000 написать, но я замучился ждать, пока комп посчитает)))
    
    for number in random_array:
        count_ls.append(predict_20(number))
    score = int(np.mean(count_ls))
    return print(f"Наш алгоритм угадывает число в среднем за: {score} попыток")

if __name__ == '__main__':
    # Запускаем программу
    score_game(predict_20)