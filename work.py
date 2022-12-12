import pandas as pd
from tqdm import trange
import pymorphy2
import matplotlib.pyplot as plt


import iterator


def read_file(elem: str)->str:
    """"reading a data from csv"""
    if elem != "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
        directory = str(elem).split(",")
        #print(len(directory))
        if len(directory) == 3:
            with open(directory[1], "r") as f:
                text = f.read()
            
            return text     
    return None


def create_table()-> pd.DataFrame:
    """create a df"""
    number_star = []
    text_opinion = []
    for i in range(1,6):
        iterator_work = iterator.Iterator("classmates1.csv", i)
        for j in trange(len(iterator.Iterator("classmates1.csv", i).list)):
            number_star.append(i)
            text_opinion.append(read_file(iterator.Iterator("classmates1.csv", i).list[j]))
    df = pd.DataFrame({
    'star': number_star,
    'text': text_opinion})
    return df


def check_table(df)-> pd.DataFrame:
    """check table to correct value"""
    print("checking")
    df.dropna()
    return df


def add_column(df)-> pd.DataFrame:
    """add_column in df """
    print("add_column")
    number_symbols_text = []
    for i in trange(len(df)):
        number_symbols_text.append(len(df.text[i]))

    df.insert(2, "len_text", number_symbols_text, False)
    return df


def statistic(df)-> None:
    """statistic in star"""
    print(df.groupby('star').count())
    

def sorted_table(df,count_words: int)->None:
    """sorted_tabel on width words"""
    df=df[df['len_text'] > count_words][['star', 'text','len_text']]
    

def table_star(df, number_star: int)->None:
    """Sorted table"""
    df=df[df['star']==number_star]


def table_star_statistic(df,number_star: int)-> None:
    """print df where star== number_star"""
    df=df[df['star']==number_star]
    print(df)
    print("кол-во слов:\nmin: " + str(df["len_text"].min()) + "\nmean: " + str(df["len_text"].mean()) 
    + "\nmax: " + str(df["len_text"].max()) )


def mnld(df)-> list:
    """Lemitization and counter words"""
    len_words = [0]*20
    morph = pymorphy2.MorphAnalyzer()
    print("Обрабатываем кол-во слов")
    for i in trange(len(df['text'])):
        words = df.text[i].split() # разбиваем текст на слова
        for word in words:
            p = morph.parse(word)[0]
            if len(p.normal_form) < len(len_words):
                len_words[len(p.normal_form)-1]+=1
    return len_words


def print_histogram(len_words: list)->None:
    """print histogram on based list"""
    len_words.insert(0,0)
    plt.plot(range(21),len_words,'vr')
    plt.ylabel('Количество слов')
    plt.xlabel('Длина слова')
    plt.title('Длина слов:')
    plt.grid(True)
    plt.xticks(range(1,20))
    plt.xlim(0)
    plt.ylim(0)
    plt.show()