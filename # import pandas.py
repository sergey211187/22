# import pandas
import pandas as pd

input_df = [{'name':'Sujeet', 'age': 10},
            {'name':'Sameer', 'age': 110},
            {'name':'Sumit','age':120}]

# создаем новый датафрейм df на основе входного датафрейма input_df и затем выводите его с помощью функции print().
df = pd.DataFrame(input_df)
print('Original DataFrame: \n', df)

# используем метод itertuples() для итерации по строкам датафрейса df и выводит значения столбцов name и age для каждой строки.
print('\nRows iterated using itertuples() :')
for row in df.itertuples():
    print(getattr(row,'name'), getattr(row, 'age'))
    