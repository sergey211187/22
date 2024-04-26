import pandas as pd

#  список со всеми строковыми значениями
lst = [['tom', 'reacher', '25'], ['krish', 'pete', '30'], ['nick', 'wilson', '26'], ['juli', 'williams', '22']]

# Создайте фрейм данных со строковыми столбцами
df = pd.DataFrame(lst, columns=['FName', 'LName', 'Age'])

print(df)