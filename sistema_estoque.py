estoque = 0

while True:
  print("Menu:")
  print("Opção 1: Adicionar ao estoque")
  print("Opção 2: Vender unidades do estoque ")
  print("Opção 3: Verificar quantidades do estoque")
  print("Opção 4: Sair")

  opcao = int(input("Digite uma opção pelo número: "))

  if opcao == 1:
    adiciona = int(input("Digite a quantidade a ser adicionado ao estoque: "))
    estoque += adiciona
    print("Quantidade", adiciona, "foi adicionado")

  elif opcao == 2:
    venda = int(input("Digite o quantidade da venda: "))
    estoque -= venda
    if estoque >= venda:
      print("Quantidade", venda, "foi vendido")
    elif estoque < venda:
      print("Quantidade para a venda insuficiente")

  elif opcao == 3:
    verifica = input("Deseja verificar o estoque ? s/n: ")
    if verifica == "s":
      print("Quantidade do estoque:", estoque)
    elif verifica == "n":
      print("Saindo da verificação...")

  elif opcao == 4:
    print("Saindo...") 
    break  

  else:
    print("Valor inválido")