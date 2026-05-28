import datetime
nome = input("Qual o seu primeiro nome: ")
sobrenome = input("Qual o seu sobrenome: ")
idade = int(input("Qual a sua idade: "))
data_atual_datetime = datetime.datetime.now()
ano_atual_datetime = data_atual_datetime.year
ano_nascimento = ano_atual_datetime - idade
altura_metros = float(input("Qual a sua altura: "))
print(f"Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade}\nAno de Nascimento: {ano_nascimento}")
print(f"Altura em metros: {altura_metros:.2f} m")
if idade >= 18:
    print(f"{nome} é maior de idade!")
    
else:
    print(f"{nome} é menor de idade!")
