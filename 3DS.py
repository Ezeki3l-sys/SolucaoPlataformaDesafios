DS = {

}
matérias = ["Matemática", "Português", "História", "Filosofia"]
quantidade = int(input("Quantos alunos quer cadastrar? \n"))
for n in range(0,quantidade):
    nome = input(f"Qual o nome do {n+1}° aluno? \n")
    DS[nome] = dict()
    for n1 in range(0,4):
        print(f"Estamos na matéria {matérias[n1]}")
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
        
        DS[nome][matérias[n1]] = lista
print(DS) 
        

        

