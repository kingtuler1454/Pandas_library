import pandas as pd
from tqdm import trange

import iterator


def read_file(elem:str):
    if elem != "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
        directory = str(elem).split(",")
        #print(len(directory))
        if len(directory)==3:
            with open(directory[1], "r") as f:
                text = f.read()
            
            return text     


def create_table():
    #df = pd.DataFrame({
    #'Количество звёзд': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    #'Текст рецензии': [18.28, 144.5, 9.485, 41.98]})
    number_star=[]
    text_opinion=[]
    
    for i in range(1,6):
        iterator_work=iterator.Iterator("classmates1.csv", i)
        for j in trange(len(iterator.Iterator("classmates1.csv", i).list)):
            number_star.append(i)
            text_opinion.append(read_file(iterator.Iterator("classmates1.csv", i).list[j]))
    df = pd.DataFrame({
    'Количество звёзд': number_star,
    'Текст рецензии': text_opinion})
    input(df)

    print("read_data")