import os
import discord
from discord.ext import tasks
import subprocess
from ServerStatus import servidor

# O Token de acesso ao Bot deverá estar em um arquivo .env
from dotenv import load_dotenv
load_dotenv('token.env')

TOKEN = os.environ.get('TOKEN_BOT', default=None)


class MineBot(discord.Client):

    client = discord.Client()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop deve ser iniciado aqui
        self.verifica_servidor.start()

    async def on_ready(self):
        print('O Bot foi logado como: {0.user}'.format(client))
        # subprocess.Popen('start_server.bat')  # Inicia o servidor de Minecraft

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
                verifica_ip = servidor.ip_publico(self)
                ip = "".join(verifica_ip)
                await message.channel.send("O endereço de ip é: **" + ip + "**")
                return

            if user_message.startswith('!status'):
                online = servidor.ServidorOnline(self)
                if online is True:
                    await message.channel.send("O servidor está **Online**")
                else:
                    await message.channel.send("O servidor está **Offline**")

    # Este loop verifica se o servidor está online e manda uma mensagem com o
    # endereço de IPV4 do servidor para o Discord no qual o bot faz parte
    @tasks.loop(seconds=10)
    async def verifica_servidor(self):

        # Inserir a ID do canal que irá receber mensagem do bot em self.get_channel()
        channel = self.get_channel(989131971290619964)
        online = servidor.ServidorOnline(self)
        try:
            if self.online is True:
                await channel.send('```O servidor está aberto.\nO IP é: ' + online[1] + '\nO ping está em: {0}'.format(round(online[2] * 100), 1) + 'ms```')

                #Início do Loop que verifica o Status do servidor após o mesmo
                # ter sido confirmado como Online
                self.verifica_status.start()
                # Uma vez que o loop encontra o servidor e envia a mensagem, o bot
                # encerra o loop
                self.verifica_servidor.stop()
        except TypeError:
            pass

    #Verifica o estado atual do servidor. Envia uma mensagem caso o mesmo fique Offline
    @tasks.loop(seconds=120)
    async def verifica_status(self):
        channel = self.get_channel(989131971290619964)
        online = servidor.ServidorOnline(self)

        try:
            if online[0] is False:
                await channel.send("O servidor **ficou Offline**")
        except TypeError:
            pass
    # Funções que previnem a execução do loop antes que o bot esteja online no servidor

    @verifica_servidor.before_loop
    async def antes_de_verificar_servidor(self):
        await self.wait_until_ready()

    @verifica_status.before_loop
    async def antes_de_verificar_status(self):
        await self.wait_until_ready()


client = MineBot()
client.run(TOKEN)
