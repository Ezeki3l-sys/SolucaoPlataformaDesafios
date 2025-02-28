import pandas as pd
import json
ds = {}

res = {}
# with open('aluno.txt','r') as file:
#    #ds = dict(arquivo.read())
#     #ds = dict(arquivo.readlines())
#     res = {key.strip(): value.strip() for key, value in (line.split(':', 1) for line in file)}

# for chave in res.keys():
#     print(chave)


with open('aluno.txt','r') as arquivo:
   ds = (arquivo.read())


print(type(ds))
print(ds)

y = json.loads(ds)
# #z = json.dumps(ds)
# #print(type(z))
# #print(z)

print(y)

print(type(y))

df = pd.read_fwf(y)


print(df)