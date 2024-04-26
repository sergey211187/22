# import pandas package
import pandas as pd

data = {'Name':['Jai','Princi','Gaurav','Anuj'],
        'Age':[27,24,22,32],
        'Adress':['Delhi','Kanpur','Allahabad','Kannauj'],
        'Qualification':['Msc','MA','MCA','Phd']
        }

df = pd.DataFrame(data)

#  выбираем строки с индексами от 1 до 3 и столбцы «Name» и «Qualification» из датафрейма df и выводим результат.
print(df.loc[1:3, ['Name', 'Qualification']])