import json
DS = {'Maria': {'Matemática': [10.0, 10.0, 10.0, 10.0, 10.0], 'Português': [10.0, 9.0, 9.0, 9.0, 9.25], 'História': [8.0, 8.0, 8.0, 8.0, 8.0], 'Filosofia': [7.0, 7.0, 7.0, 7.0, 7.0]}, 'Vitor': {'Matemática': [6.0, 6.0, 6.0, 6.0, 6.0], 'Português': [5.0, 5.0, 5.0, 5.0, 5.0], 'História': [4.0, 4.0, 4.0, 4.0, 4.0], 'Filosofia': [3.0, 3.0, 3.0, 3.0, 3.0]}}

r = json.dumps(DS)

print(r)

print(type(r))

