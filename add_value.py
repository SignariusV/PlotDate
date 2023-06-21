from datetime import date

name='weight'

value=input('Введите новое значение:')
today = date.today().strftime('%Y,%m,%d')
with open(f'{name}.txt', 'a') as file:
    file.write(f'\n{today}_{value}')
import main