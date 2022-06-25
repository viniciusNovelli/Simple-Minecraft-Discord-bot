import requests


# Busca o ip público do PC no qual o script está sendo executado
def ip_publico():
    ip_publico = str(requests.get('https://api.ipify.org/').text)
    return ip_publico
