from exceptions.custon_exception import ErroCustomizado

class Calcula:
    '''Construtor'''
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    '''Somar'''
    def somar(self) -> float:
        operacao = None
        try:
            operacao = self.num1 + self.num2
            
            self.__validar_operacao(operacao)
            
        except ErroCustomizado as exception:
            print(exception)

        except Exception as exception:
            print(exception)

    '''Subtrair'''
    def subtrair(self) -> float:
        operacao = None
        try:
            operacao = self.num1 - self.num2

            self.__validar_operacao(operacao)

        except ErroCustomizado as exception:
            print(exception)

        except Exception as exception:
            print(exception)

    '''Multiplicar'''
    def multiplicar(self) -> float:
        operacao = None
        try:
            operacao = self.num1 * self.num2

            self.__validar_operacao(operacao)

        except ErroCustomizado as exception:
            print(exception)

        except Exception as exception:
            print(exception)

    '''Dividir'''
    def dividir(self) -> float:
        operacao = None
        try:
            operacao = self.num1 / self.num2

            self.__validar_operacao(operacao)

        except ZeroDivisionError:
            print("Não é possível dividir por zero!\n")

        except ErroCustomizado as exception:
            print(exception,"\n")

        except Exception as exception:
            print(exception, "\n")    

    '''Formatar resultado'''
    def __formatar_operacao(self, operacao: float) -> None:        
        print(f"Resultado: {operacao: .2f}\n")


    '''Validar campos e o valor do resultado'''
    def __validar_operacao(self, operacao: float) -> None:
        if self.num1 < 0 or self.num2 < 0:
            raise ErroCustomizado("Não pode haver valores menor do que zero\n")
        elif operacao < 0:
           raise ErroCustomizado("O resultado não pode ser negativo\n")
        else:
            self.__formatar_operacao(operacao)
   