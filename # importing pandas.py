# importing pandas
import pandas as pd

# создаем лист
input_df=[{'name':'Sujeet', 'age':10},
          {'name':'Sameer', 'age':11},
          {'name':'sumit', 'age':12}]

# создаем пустой DataFrame с помощью библиотеки pandas. DataFrame - это двумерная структура данных, аналогичная таблице.
df=pd.DataFrame(input_df)
print('Original Dataframe: \n', df)

# используем метод iterrows() для итерации по строкам датафрейса df и вывода значений столбцов name и age для каждой строки.
print('\nRows iterated using iterrows():')
for index, row in df.iterrows():
    print(row['name'], row['age'])