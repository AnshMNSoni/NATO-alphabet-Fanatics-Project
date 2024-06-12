import pandas as pd

file = pd.read_csv('./NATO-alphabet-Fanatics-project/data.csv')

name = input('Enter your name here:').upper()

fanatics = [file['code'][ord(ch) - 65] for ch in name]
print(fanatics)