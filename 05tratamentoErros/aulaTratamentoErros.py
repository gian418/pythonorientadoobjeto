"""
try:
    x = int(input('Digite um numero: '))
except:
    print('Deu erro, insira apenas numeros')
    x = 0
finally:
    print(f'O valor digitado foi {x}')
"""


class ValorRepetidoErro(Exception):

    def __init__(self, n):
        self.num = n

    def __str__(self):
        return f'Vixe! Você já digitou o {self.num}'


def main():
    lista = []
    for i in range(8):
        while True:
            try:
                num = int(input('Digite um numero: '))
                break
            except ValueError:
                print('Digite apenas numeros')

        if num not in lista:
             lista.append(num)
        else:
            raise ValorRepetidoErro(num)


main()