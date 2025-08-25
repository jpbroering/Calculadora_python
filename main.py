# Recebe um operador Aritmético e retorna uma função
def calcular(opcao):
    # retorna os valores de entrada em valores do tipo ponto flutuante, caso seja impossível, retorna falso
    def calculo(a, b):
        try:
            return float(a), float(b)
        except ValueError:
            return False
    # Retorna a soma de A e B caso sejam números com ponto flutuante
    def somar(a, b):
        a,b = calculo(a,b)
        return a + b if isinstance(a,(int, float)) and isinstance(b,(int, float)) else False
    
    # Retorna a soma de A e B caso sejam números com ponto flutuante
    def subtrair(a, b):
        a,b = calculo(a,b)
        return a - b if isinstance(a,(int, float)) and isinstance(b,(int, float)) else False
    
    # Retorna a soma de A e B caso sejam números com ponto flutuante
    def multiplicar(a, b):
        a,b = calculo(a,b)
        return a * b if isinstance(a,(int, float)) and isinstance(b,(int, float)) else False
    
    # Retorna a soma de A e B caso sejam números com ponto flutuante
    def dividir(a, b):
        a,b = calculo(a,b)
        return a / b if isinstance(a,(int, float)) and isinstance(b,(int, float)) else False
    
    if opcao == "+":
        return somar
    elif opcao == "-":
        return subtrair
    elif opcao == "*":
        return multiplicar
    elif opcao == "/":
        return dividir
    else:
        False

# Exibe a interface da calculadora e retorna a entrada do usuário
def opcoes():
    MENSAGEM = """\t### Calculadora ###

    [+]\tSomar
    [-]\tSubtrair
    [*]\tMultiplicar
    [/]\tDividir

    Opção: """
    return input(MENSAGEM)

def main():
    opcao = opcoes()

    num_a = input("Digite o primeiro valor: ")
    num_b = input("Digite o segundo valor: ")
    print(calcular(opcao)(num_a, num_b))

main()