import work


def main():
    df = work.create_table()
    df = work.check_table(df)
    df = work.add_column(df)
    work.statistic(df)
    work.sorted_table(df, 350)
    work.table_star(df, 4)
    work.table_star_statistic(df, 4)
    hist_info = work.create_hist(df, 4)
    work.print_histogram(dict(hist_info[-10:]))


if __name__ == "__main__":
    main()




