import pandas as pd
from tqdm import trange
import pymorphy2
import matplotlib.pyplot as plt

import iterator


def create_table() -> pd.DataFrame:
    """create a df"""
    number_star = []
    text_opinion = []
    for i in range(1, 6):
        iterator_work = iterator.Iterator("classmates1.csv", i)
        for j in trange(len(iterator.Iterator("classmates1.csv", i).list)):
            number_star.append(i)
            text_opinion.append(
                read_file(iterator.Iterator("classmates1.csv", i).list[j])
            )
    df = pd.DataFrame({"star": number_star, "text": text_opinion})
    return df


def read_file(elem: str) -> str:
    """ "reading a data from csv"""
    if elem != "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
        directory = str(elem).split(",")
        # print(len(directory))
        if len(directory) == 3:
            with open(directory[1], "r") as f:
                text = f.read()

            return text
    return None


def check_table(df: pd.DataFrame) -> None:
    """check table to correct value"""
    print("checking")
    df = df.dropna()
    print(df.info())
    return df


def add_column(df) -> pd.DataFrame:
    """add_column in df"""
    print("add_column")
    number_symbols_text = []
    for i in trange(len(df)):
        number_symbols_text.append(len(df.text[i]))

    df.insert(2, "len_text", number_symbols_text, False)
    return df


def statistic(df: pd.DataFrame) -> None:
    """statistic in star"""
    print(df.describe())


def sorted_table(df: pd.DataFrame, count_words: int) -> None:
    """sorted_tabel on width words"""
    return df[df["len_text"] > count_words][["star", "text", "len_text"]]


def table_star(df: pd.DataFrame, number_star: int) -> None:
    """Sorted table"""
    return df[df["star"] == number_star]


def table_star_statistic(df: pd.DataFrame, number_star: int) -> None:
    """print df where star== number_star"""
    df = df[df["star"] == number_star]
    print(df)
    print(
        "кол-во слов:\nmin: "
        + str(df["len_text"].min())
        + "\nmean: "
        + str(df["len_text"].mean())
        + "\nmax: "
        + str(df["len_text"].max())
    )


def create_hist(df: pd.DataFrame, number_star: int) -> list:
    """Lemitization and counter words"""
    words = []  # для леминитизированных слов
    lonely_words_count = []  # для подсчета вхождений каждого слова
    morph = pymorphy2.MorphAnalyzer()
    print("Обрабатываем кол-во слов")
    for i in trange(len(df[df["star"] == number_star])):
        words_list = (df.text[i]).split()  # разбиваем текст на слова
        for word in words_list:
            p = morph.parse(word)[0]
            words.append(p.normal_form)

    lonely_words = list(set(words))  # слова без повторений
    for element in lonely_words:
        lonely_words_count.append(words.count(element))
    book = dict(zip(lonely_words_count, lonely_words))
    return sorted(book.items())  # вернем остортированный  словарь


def print_histogram(hist_info: dict) -> None:
    """print histogram on based dict"""
    plt.ylabel("Используемое количество")
    plt.xlabel("слово")
    plt.title("Популярность слов:")
    plt.grid(True)
    plt.bar(hist_info.values(), hist_info.keys())
    plt.show()
