# Estudo sobre encapsulamento e propriedades com uma única classe

class Transacao:
    def __init__(self, valor=0, descricao='Sem Descrição'):
        # Encapsulando todos os atributos
        self._valor = valor
        self._descricao = descricao


    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor < 0:
            print('O valor não pode ser menor que zero')
        else:
            self._valor = valor

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        # Verificação para entradas não vazias
        if not descricao:
            print('A descrição não pode ser vazia!')
        # Definição de tamanho para a descrição
        elif len(descricao) > 15:
            print('A descrição não pode ter mais de 15 caracteres')
        else:
            self._descricao = descricao



# t = Transacao(0,'')
t = Transacao()

t.descricao = 'Guilherme'
t.valor = -1000

print(t.descricao)
print(t.valor)

t.descricao = 'Antonio'

print(t.descricao)







