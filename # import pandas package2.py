# import pandas package
import pandas as pd

# Определяем словарь, содержащий данные о сотрудниках

data = {'Name':['Jai','Princi','Gaurav','Anuj'],
        'Age':[27,24,22,32],
        'Adress':['Delhi','Kanpur','Allahabad','Kannauj'],
        'Qualification':['Msc','MA','MCA','Phd']
        }

# Преобразовываем словарь в DataFrame
df = pd.DataFrame(data)

#.метод фрейма данных loc
# фильтрация строк и выбор столбцов по формату меток
# df.loc[строки, столбцы]
# строка 1, все столбцы
print(df.loc[0,:])