import msvcrt
import datetime
import csv


protecao = input('digite a senha:' + '\n')
if protecao == '123':
    print('Acesso liberado meu patrão')
elif protecao == '456':
    print('Acesso liberado patroa')
else:
    print('Acesso negado')
    exit()

print('''
      

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//*/*/*/*/*/*/*/*//*/*/*/*/      
*/*/*/*/*/*/*/*/ URNA ELETRONICA MODERNA   /*/*/*/*/*/*/*/*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//*/*/*/*/*/*/*/*//*/*/*/
      ''')


candidatos = []

print('''
     1 - listar candidatos
     2 - cadastrar candidatos
     3 - banir candidatos safados
      ''')

candidato = input('Digite o nome do candidato:')
numero_candidato = int(input('Digite o número do candidato:'))

def cadastro_candidatos(candidato, numero_candidato):
    with open('candidatos.csv', 'a') as db:
        return (candidato, numero_candidato)

while True:  # Loop indefinido para continuar verificando um pressionamento de tecla
    answer = msvcrt.getch()  # Aguardar pressionamento de tecla

    if answer == b'1':  # Se '1' for pressionado
        with open('candidatos.csv', 'r') as db:
            reader = csv.reader(db)
            for row in reader:
                print(row)
        break  # Sair do loop após responder
    elif answer == b'2':  # Se '2' for pressionado
        cadastro_candidatos(candidato, numero_candidato)
        print ('Candidato cadastrado com sucesso', candidato, numero_candidato)
        break  # Sair do loop após responder
    elif answer == b'3':  # Se '3' for pressionado
        print("bar")
        break  # Sair do loop após responder

