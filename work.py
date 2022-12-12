import pandas as pd
from tqdm import trange
import pymorphy2
import matplotlib.pyplot as plt

import iterator


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


df=create_table()


def check_table(df:pd.DataFrame)->None:
    """check table to correct value"""
    print("checking")
    df=df.dropna()
    print(df.info())
    return df


df=check_table(df)


def add_column(df)-> pd.DataFrame:
    """add_column in df """
    print("add_column")
    number_symbols_text = []
    for i in trange(len(df)):
        number_symbols_text.append(len(df.text[i]))

    df.insert(2, "len_text", number_symbols_text, False)
    return df


df=add_column(df)

def statistic(df: pd.DataFrame)-> None:
    """statistic in star"""
    print(df.describe())


statistic(df)


def sorted_table(df: pd.DataFrame,count_words: int)->None:
    """sorted_tabel on width words"""
    df=df[df['len_text'] > count_words][['star', 'text','len_text']]
    print(df)
    return df

sorted_table(df,350)


def table_star(df: pd.DataFrame, number_star: int)->None:
    """Sorted table"""
    print(df[df['star']==number_star])
    return df[df['star']==number_star]

    
df=table_star(df,4)

def table_star_statistic(df: pd.DataFrame, number_star: int)-> None:
    """print df where star== number_star"""
    df=df[df['star']==number_star]
    print(df)
    print("кол-во слов:\nmin: " + str(df["len_text"].min()) + "\nmean: " + str(df["len_text"].mean()) 
    + "\nmax: " + str(df["len_text"].max()) )

table_star_statistic(df,4)


def create_hist(df : pd.DataFrame)-> list:
    """Lemitization and counter words"""
    #df=df[df['star']==number_star]
    words = []
    morph = pymorphy2.MorphAnalyzer()
    print("Обрабатываем кол-во слов")
    for i in trange(len(df['text'])):
        df.text[i].split() # разбиваем текст на слова
        for word in words:
            p = morph.parse(word)[0]
            words.append(p.normal_form)
    lonely_words=list(set(words))
    print(lonely_words)    
    #return words

create_hist(df)

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

print_histogram(len_words)