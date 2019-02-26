class Animal:
    def __init__(anim, cor, genero, andar):
        anim.cor = cor
        anim.genero = genero
        anim.numero_de_patas = andar

    def falar(anim):
        print('Olá sou um cachorro e sei falar')

    def andar(anim):
        print(f'Estou andando sobre {anim.numero_de_patas}')

    def amamentar(anim):
        if anim.genero.lower() [0] == 'm':
            print('Machos não amamentam')
            return
        print('Amamentando meu filhote')


#Rex = Animal('marron', 'feminino', 4)
#Rex.falar()
#Rex.andar()
#Rex.amamentar()


class Pessoa(Animal):
    def __init__(anim, cor, genero, andar, cabelo):
        super(Pessoa, anim).__init__(cor, genero, andar)
        anim.cabelo = cabelo

    def falar(anim):
        super(Pessoa, anim).falar()
        print('Olá sou uma pessoa e sei falar')


Hugo = Pessoa('branco', 'masculino', 2, 'castanho')
Hugo.falar()