#Importações
import time
#Final do programa
def final():
  mensagem = 'Obrigado, volte sempre!'
  print('\n', '>>', mensagem.center(30) + '<<')
#Tupla com os ítens da loja
produtos = ('Lápis', 1.50,
'Mochila', 150.98,
'Caderno', 20.38,
'Borracha', 2,
'Lapiseira', 3,
'Estojo', 10,
'Adesivos', 0.5,
'Lápis/colorir', 1.99)
#Váriaveis e lista que recebe os dados
total = 0
lista = []
soma = 0
#Repetir enquanto usuario digitar S (sim)
while True:
  print('\033[1;33m=\033[m'*40)
  print(f'\033[1;36m{"Material Escolar":^37}\033[m')
  print('\033[1;33m=\033[m'*40, '\n')
#Mostrar os produtos formatados 
  for p in range(0, len(produtos)):
    if p %2 == 0:
      print('{:.<30}R$ '.format(produtos[p]), end='')
    else:
      print('{:.2f}'.format(produtos[p]))
#Opção de escolha      
  print("""\nComo deseja comprar:
[ V ] varias vezes o mesmo produto
[ C ] comprar vários produtos
  """)
  escolha = str(input('Informe sua escolha: ')).upper()[0]
#Validação de resposta
  while escolha not in 'V' and escolha not in 'C':
    escolha = str(input('Opção inválida! Informe sua escolha: ')).upper()[0]
#Resposta para opção V
  if escolha == 'V':
    nomep = str(input('\nInforme o nome do produto: ')).capitalize()
    unidade = int(input('\nInfome quantas unidades você quer: '))
    preco = float(input('\nInforme o preço do produto: '))
    total = preco * unidade
    print('\n\033[1;32mCalculando o valor a pagar...\033[m')
    time.sleep(2)
    print('\nO total a ser pago é \033[4mR${:.2f}\033[m'.format(total))
#Resposta para a opção C
  elif escolha == 'C':
    quant = int(input('Informe a quantidade de produtos: '))
#Retirá pedindo o nome do produto de acordo com a quantidade------
    for x in range(1, quant + 1):
      prod = str(input('Informe o nome do {}º produto que você quer: '.format(x))).capitalize()
    print('\n')
#Repetirá pedindo o preço de acordo com a quantidade
    for y in range(1, quant + 1):
      precop = float(input('Informe o preço: '))
      lista.append(precop)
#Fará a soma de todos os preços
    for i in lista:
      soma = soma + i
#Saída do total a pagar
    print('\033[1;32mProcessando o total...\033[m\n')
    time.sleep(2)
    print('O total a pagar é \033[4mR${:.2f}\033[m'.format(soma))
#Escolha se quer continuar a comprar
  again = str(input('\nDeseja mais alguma coisa? [S/N]: ')).upper()
#Validação
  while again.strip() not in 'S' and again.strip() not in 'N':
    again = str(input('Comprar dnv? [S/N]: ')).upper()
#Fim do programa se for digitado N
  if again == 'N':
    break
#Função chamada que mostra o final
final()
