import pandas as pd
from tqdm import trange
import pymorphy2

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
    mnld(df)
   #check_table(df)


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
    sorted_table(df,350)


def sorted_table(df,count_words):
    df=df[df['len_text'] > count_words][['star', 'text','len_text']]
    table_star_statistic(df, 4)

def table_star(df, number_star):
    df=df[df['star']==number_star]


def table_star_statistic(df,number_star):
    df=df[df['star']==number_star]
    print(df)
    print("кол-во слов:\nmin: "+str(df["len_text"].min())+"\nmean: "+str(df["len_text"].mean())+"\nmax: "+str(df["len_text"].max()) )


def mnld(df):
    len_words=[0]*20
    morph = pymorphy2.MorphAnalyzer()
    for i in trange(len(df['text'])):
        words = df.text[i].split() # разбиваем текст на слова
        for word in words:
            p = morph.parse(word)[0]
            if len(p.normal_form)<len(len_words):
                len_words[len(p.normal_form)-1]+=1

    print(len_words)

    