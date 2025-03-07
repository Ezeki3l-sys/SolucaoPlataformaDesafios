import json
import os.path
DS = {
}
if os.path.isfile('aluno.txt') == False:
    print("Não existe")
else:
    with open('aluno.txt', 'r',  encoding="utf-8") as file:
        DS = json.load(file)
   

    materias = ["Matemática", "Português", "História", "Filosofia"]
    quantidade = int(input("Quantos alunos quer cadastrar? \n"))
    for n in range(0,quantidade):
        while True:
            nome = input(f"Qual o nome do {n+1}° aluno? \n")
            if not(DS.get(nome)):
                break
            else:
                print("Usuário já existe. Informe outro nome... \n")
        print(DS.get(nome))
        DS[nome] = dict()
        for n1 in range(0,4):
            print(f"Estamos na matéria {materias[n1]}")
            lista = []
            nota2 = 0
            nota = -1
            for n in range(1,5):
                nota = -1
                while(nota<0 or nota>10):
                    nota = float(input(f"Digite a {n}° nota: \n"))
                nota2 = nota2+nota
                lista.append(nota)
            media = nota2/4
            lista.append(media)
            
            DS[nome][materias[n1]] = lista


    print(DS)
    r = json.dumps(DS, ensure_ascii=False)
    print(r)
    with open('aluno.txt','w', encoding="utf-8") as arquivo:
        arquivo.write(r)

# for aluno in DS.values():
#     print(aluno)
#     chamada.append(aluno)
# print(chamada)
# sala = str(DS)
# print(sala)
# with open('aluno.txt','w') as arquivo:
#     arquivo.write(sala)
#     arquivo.close



# with open('aluno.txt','a', encoding="utf-8") as arquivo:
#    for aluno in chamada:
#     arquivo.write(f"{aluno}\n")

        

        

