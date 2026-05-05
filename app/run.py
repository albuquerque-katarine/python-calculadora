from model.calcula import Calcula

'''Impressão do menu de opções'''
def imprimir_opcoes() -> None:
    print('''Escolha uma opção:
      1 - Soma
      2 - Subtração
      3 - Multiplicação
      4 - Divisão
      5 - Sair''')

'''A opção é informada e armazenada em variável, logo retornada pela função'''
def informe_opcao() -> int:
    opcao = int(input("Opção: "))
    return opcao

'''De acordo com a opção é reacizadas as operações de soma,subtração,multiplicação e divisão'''
def escolher_opcao(opcao: int, num1: float, num2: float) -> None:
    if opcao == 1:
        calc = Calcula(num1,num2)
        calc.somar()
    elif opcao == 2:
        calc = Calcula(num1,num2)
        calc.subtrair()
    elif opcao == 3:
        calc = Calcula(num1,num2)
        calc.multiplicar()
    elif opcao == 4:
        calc = Calcula(num1,num2)
        calc.dividir()
    else:
        print("Opção inválida!")

'''Pega os valores digitados e adiciona no objeto da classe Calcula'''
def get_valores(opcao: int) -> None:    
    
    print("\nInforme os valores:\n")  

    num1 = float(input("Valor 1: "))
    num2 = float(input("Valor 2: "))

    escolher_opcao(opcao, num1, num2)

'''Realiza o cálculo'''
def calcular() -> None:

    contador = 1

    imprimir_opcoes()
    opcao = informe_opcao()    

    while opcao < 5 and opcao > 0:

        get_valores(opcao)

        contador += 1

        imprimir_opcoes()
        opcao = informe_opcao()  

'''Executa a calculadora'''
print("\n### Calculadora Simples ###\n")
calcular()
print("\n### Finalizada ###\n")