import msvcrt
import datetime
import csv


protecao = input('digite a senha:')
if protecao == '123':
    print('Acesso liberado meu patrão')
elif protecao == '456':
    print('Acesso liberado meu patroa')
else:
    print('Acesso negado')

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

while True:  # Loop indefinido para continuar verificando um pressionamento de tecla
    answer = msvcrt.getch()  # Aguardar pressionamento de tecla

    if answer == b'1':  # Se '1' for pressionado
        with open('candidatos.csv', 'r') as db:
            reader = csv.reader(db)
            for row in reader:
                print(row)
        break  # Sair do loop após responder
    elif answer == b'2':  # Se '2' for pressionado
        with open('candidatos.csv', 'a') as db:
            candidato = input('Digite o nome do candidato:', 'Digite o partido do candidato:' , 'Digite o número do candidato:')
            candidatos.append(candidato)
            escreva = csv.writer(db)
            escreva.writerow(candidato)
        break  # Sair do loop após responder
    elif answer == b'3':  # Se '3' for pressionado
        print("bar")
        break  # Sair do loop após responder

