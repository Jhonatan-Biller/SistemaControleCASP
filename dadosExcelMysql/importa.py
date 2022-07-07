import pandas as pd
import os

os.chdir(r'C:\Users\Jhonatan\Documents\GitHub\SistemaControleCASP\dadosExcelMysql')

df = pd.read_excel('dados.xlsx')

print(df)