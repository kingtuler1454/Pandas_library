import pandas as pd


def read_data():
    df = pd.DataFrame({
    'Звезда': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'Заголовок': [18.28, 144.5, 9.485, 41.98],
    'Преимущества': [2725000, 17100000, 207595, 603628],
    'Недостатки': [18.28, 144.5, 9.485, 41.98],
    'Отзыв': [18.28, 144.5, 9.485, 41.98]})

    print(df)
    print("read_data")