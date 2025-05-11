print('Calculadora!!!')
n1 = int(input('Digite um Valor pra Calculadora: '))
print('|÷|x|-|+|')
s = str(input('Digite um símbolo pra Calculadora: '))
n2 = int(input('Digite um Valor pra Calculadora: '))
res = 0
if s == '÷':
    res =  n1 / n2
if s == 'x':
    res =  n1 * n2
if s == '-':
    res =  n1 - n2
if s == '+':
    res =  n1 + n2
print('{} {} {} = {}'.format(n1,s,n2,res))
