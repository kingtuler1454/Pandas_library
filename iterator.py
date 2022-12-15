import os
import re
import csv
from typing import Optional


class Iterator:
    def __init__(self, way_to_csv_file: str, name_class: str):
        self.name_class = str(name_class)
        self.list = []
        self.way_to_file = way_to_csv_file
        self.counter = 0

        file = open(self.way_to_file, "r", encoding="utf-8")
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            if str(row)[-3] == self.name_class:
                self.list.append(row)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.list):
            self.counter += 1
            return self.list[self.counter - 1]
        else:
            return ""
