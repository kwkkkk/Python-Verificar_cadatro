nome = str(input('Digite seu nome: '))
idade = int(input(f'Digite sua idade, {nome}: '))
peso = float(input(f'digite o seu peso, em kilogramas(kg): '))
altura = float(input('Digite sua altura em metros(m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'{nome}, seu imc é {imc:.2f}, você está muito abaixo de seu peso ideal.')
elif imc >= 18.5 and imc <25:
    print(f'{nome}, seu imc é {imc:.2f}, você está no seu peso ideal.')
elif imc >= 25 and imc <30:
    print(f'{nome}, seu imc é {imc:.2f}, você está acima do seu peso.')
elif imc >= 30 and imc <35:
    print(f'{nome}, seu imc é {imc:.2f}, você está muito acima do peso.')
elif imc >= 35 and imc <= 40:
    print(f'{nome}, seu imc é {imc:.2f}, você está muito obeso...')
else:
    print(f'KRLH {nome}, OBESO PRA KRLH KKKKKKKKKKKKKKKKKKKK.')





