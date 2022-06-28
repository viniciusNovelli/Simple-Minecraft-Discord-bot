# A biblioteca "Minecraft Server" Será retirada do ar em Agosto de 2022
# Outra forma de verificar o servidor será necessária
from mcstatus import MinecraftServer
import requests


# Verifica se o servidor está online
# Se latency retornar o erro de Timeout, o servidor está offline
class servidor():
    def __init__(self):
        self.online = False
        self.latencia = ''
        self.ip = ''

    def __str__(self):
        return self.latencia

    def ServidorOnline(self):
        ip_pub = servidor.ip_publico(self)

        try:
            server = MinecraftServer.lookup(ip_pub)
            self.online = True
            self.ip = servidor.ip_publico(self)
            self.latencia = server.ping()
            print(
                'O servidor está online e seu ping é de {0} ms'.format(self.latency))
        except TimeoutError:
            print("O Servidor está Offlile")
            self.online = False

    def ip_publico(self):
        self.ip = str(requests.get('https://api.ipify.org/').text)
        return self.ip
