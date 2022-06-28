# Simple Minecraft Discord bot
 Bot simples que inicia um servidor no Minecraft através de um arquivo .BAT e notifica os membros de um server no Discord quando ele estiver online, além de também mostrar qual o IPV4 para conexão.


# IMPORTANTE:

1- Após criar sua aplicação no Discord e baixar o código base, crie um arquivo .env que armazene o seu Token de acesso ao Bot. Esse arquivo é crucial para manter o sigilo do seu acesso.

2- Para iniciar corretamente, edite o arquivo 'start_server.BAT' com o caminho do executável do servidor, o arquivo .BAT equivalente, ou os argumentos que seriam inseridos no CMD para iniciar o servidor.

3- Antes de iniciar o bot pela primeira vez, edite o código com o nome do canal no qual o bot poderá responder a comandos e enviar mensagens e a ID do mesmo para que o bot possa enviar determinadas mensagens dependendo do comportamento do servidor.


Obs: O passo 3 logo será automatizado numa futura atualização (há um pequeno spoiler do que pretendo fazer no arquivo funcoes_bot.py).

# Módulos que estou utilizando:

API do Discord:
py -3 -m pip install -U discord.py
Link da documentação:
https://discordpy.readthedocs.io/en/stable/index.html

Módulo que se comunica especificamente com servidores de Minecraft*:
python3 -m pip install mcstatus
Link da documentação:
https://github.com/py-mine/mcstatus/tree/1456bb1de785c4d92b34260958f48e7287b5f45f

*Segundo o desenvolvedor, este módulo será removido em agosto de 2022. Outra atualização a este código trará uma forma de comunicar-se com o servidor de Minecraft.
