from Ping import ip_publico
from ServerStatus import ServidorOnline
import discord
from discord.ext import tasks
import subprocess


# Insira aqui o TOKEN de acesso do seu BOT
TOKEN = ''


class MineBot(discord.Client):

    client = discord.Client()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop deve ser iniciado aqui
        self.verifica_servidor.start()

    async def on_ready(self):
        print('O Bot foi logado como: {0.user}'.format(client))
        subprocess.Popen('start_server.bat')  # Inicia o servidor de Minecraft

    # O ".event" é acionado toda vez que algo acontece dentro do servidor no
    # Discord. Neste caso, quando uma mensagem for enviada.
    @client.event
    async def on_message(self, message):
        user_message = str(message.content)  # <- Recebe o conteúdo da mensagem

        # Garante que o Bot não responda a si mesmo
        if message.author.id == self.user.id:
            return
        # Garante que o bot apenas responderá no canal correto
        if message.channel.name == 'bots':
            # Verifica o comando do usuário e envia uma mensagem com o retorno
            # desejado.
            if user_message.startswith('!ip'):
                await message.channel.send("O endereço de ip é: " + ip_publico())
                return

    # Este loop verifica se o servidor está online e manda uma mensagem com o
    # endereço de IPV4 do servidor para o Discord no qual o bot faz parte
    @tasks.loop(seconds=10)
    async def verifica_servidor(self):
        
        channel = self.get_channel() # <- Inserir a ID do canal que irá receber mensagem do bot em self.get_channel(1234556789)
        ping = ServidorOnline()
        if ping > 0:
            await channel.send('O servidor está aberto, e o IP é: ' + ip_publico())
            # Uma vez que o loop encontra o servidor e envia a mensagem, o bot encerra o loop
            self.verifica_servidor.stop()

    # Função que previne a execução do loop antes que o bot esteja online no servidor
    @verifica_servidor.before_loop
    async def antes_de_verificar_servidor(self):
        await self.wait_until_ready()


client = MineBot()
client.run(TOKEN)
