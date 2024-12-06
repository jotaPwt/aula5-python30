# Crie um sistema de notas, com as seguintes operações:

# ***** Utilize While ou loop *****

# # Sistema de notas de alunos

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga a conta bloqueada 
# - Inserir notas 
# - Fazer a média


print('Sistema de nota Iniciado')
cadastro = []

login_cad = input('Cadastre-se no sistema: ')
login_senha = int(input('Cadastre sua senha: '))
cadastro.append(login_cad)
cadastro.append(login_senha)
print(cadastro)

for i in range(0, 5):
    usuario = str(input('Digite seu Usuario: '))
    senha = int(input('Digite sua senha: '))
    if usuario in cadastro and senha in cadastro:
        print('Acesso liberado')
        break
    else:
        print('Acesso negado, tente novamente')
        usuario = input('Digite seu Usuario: ')
        senha = int(input('Digite sua senha: '))
        if i == 0:
            print('Voce excedeu o limite de tentativas, sua conta foi bloqueada.')
            break
        else:
            usuario = input('Digite seu Usuario: ')
            senha = int(input('Digite sua senha: '))


lista_notas = []
for n in range(0,4):
    
    nota = int(input('Digite sua nota: '))
    lista_notas.append(nota)
    print(lista_notas)
   
media = sum(lista_notas) / len(lista_notas)
print(f'A sua média é {media}')