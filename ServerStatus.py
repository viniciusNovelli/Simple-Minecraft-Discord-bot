# A biblioteca "Minecraft Server" Será retirada do ar em Agosto de 2022
# Outra forma de verificar o servidor será necessária
from mcstatus import MinecraftServer
from Ping import ip_publico


# Verifica se o servidor está online
# Se latency retornar 0, o servidor está offline
def ServidorOnline():
    ip_pub = ip_publico()
    server = MinecraftServer.lookup(ip_pub)
    latency = server.ping()
    print('O servidor está online e seu ping é de {0} ms'.format(latency))
    return latency
