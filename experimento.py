import pandas as pd
import json


with open('aluno.txt', 'r',  encoding="utf-8") as file:
    data = json.load(file)

print(data)


