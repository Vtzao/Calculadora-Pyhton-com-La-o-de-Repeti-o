#Exercicio 5.1.1 /// Calculadora usando laço de repetição WHILE True / break / continue
##Menu
print('Calculadora:')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

##Condicionais
while True:
    op = input('Qual operação deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}' .format(x, y, res))
        continue
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}' .format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}' .format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}' .format(x, y, res))
        continue
    elif (op == 's'):
        break
    else:
        print('Operação Inválida!')

print('Encerrando o programa...')
