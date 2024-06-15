import pandas as pd

file = pd.read_csv('data.csv')

def phonetics():
    try:
        name = input('Enter your name here:').upper()
        fanatics = [file['code'][ord(ch) - 65] for ch in name]
        
    except KeyError:
        print('Sorry! only letters in the alphabet please!')
        phonetics()
    
    else:
        print(fanatics)

phonetics()