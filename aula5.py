def calculo_imc():
    print('-----------------CALCULADORA IMC----------------------')
    peso = int(input('digite seu peso: '))
    altura = float(input('Digite sua Altura: '))
    calculo = peso // altura ** 2
    print(f'seu imc é {calculo}')


    if calculo < 22:
        print('Abaixo do peso ideal')
    elif calculo >= 22 and calculo <= 27:
        print('Peso ideal')
    elif calculo > 27 and calculo < 29.9:
        print('Sobrepeso')
    elif calculo > 30:
        print('Obesidade')
    else:
        print('Digite algo valido')
        
        calculo_imc()

try:
        calculo_imc()
except:
    print('digite algo valido')
    voltar = input('Deseja voltar? s/n')
         
    if voltar == 's':
        calculo_imc()
    elif voltar == 'n':
        input('Fechar programa')