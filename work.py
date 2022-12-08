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
    return None

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
    'star': number_star,
    'text': text_opinion})
    check_table(df)


def check_table(df):
    print("checking")
    df.dropna()
    add_column(df)

def add_column(df):
    print("add_column")
    number_symbols_text=[]
    for i in trange(len(df)):
        number_symbols_text.append(len(df.text[i]))

    df.insert(2,"len_text",number_symbols_text,False)
    statistic(df)


def statistic(df):
    print(df.groupby('star').count())