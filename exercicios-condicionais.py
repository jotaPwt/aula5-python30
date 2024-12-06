# Exercício 1: Verificação de Número Positivo
# Escreva um programa em Python que solicite ao usuário um número inteiro e verifique 
# se o número é positivo, negativo ou zero. 
# Em seguida, exiba uma mensagem apropriada de acordo 
# com o resultado da verificação.

n1 = int(input('Digite um numero: '))

if n1 / 2 > 0:
    print('Numero positivo')
else:
    print('Numero negativo')


# Exercício 2: Classificação de Triângulos
# Escreva um programa em Python que receba três comprimentos de 
# lados de um triângulo e determine se o triângulo é equilátero, isósceles ou escaleno.

c1 = int(input('Digite um lado do triangulo: '))
c2 = int(input('Digite um lado do triangulo: '))
c3 = int(input('Digite um lado do triangulo: '))

if c1 == c2 and c2 == c3:
    print('Triangulo Equilátero')
elif c1 == c2 and c3 != c1:
    print('Triangulo Isóceles')
else:
    print('Triangulo Escaleno')

# Exercício 3: Verifique se o usuário é maior de idade e pode entrar no show, escreva 
# um programa que peça a usuário a idade e decida se ele pode entrar no show. Sistema 
# bem estruturado.  


idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Maior de idade. Permitido')
elif idade < 18:
    print('Menor de idade. Não Permitido')