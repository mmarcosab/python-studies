class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if (valor <= (self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def gerar_extrato(self):
        print("Saldo de {} {}".format(self.titular, self.saldo))

    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def codigo_banco(self):
        return self.__codigo_banco

