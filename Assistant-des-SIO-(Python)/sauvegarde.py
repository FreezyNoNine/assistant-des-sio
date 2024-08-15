import discord
from discord.ext import commands
import pronotepy
from pronotepy.ent import ent_auvergnerhonealpe
import datetime

class MyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await self.tree.sync()

    async def on_ready(self) -> None:
        print("Je suis en ligne")


bot = MyBot()

client = None  # Initialize client globally

@bot.tree.command(name="connexion", description="Se connecter à son compte pronote")
async def connexion(interaction: discord.Interaction, username: str, password: str):
    global client
    client = pronotepy.Client('https://0382780r.index-education.net/pronote/eleve.html',
                                username=username,
                                password=password,
                                ent=ent_auvergnerhonealpe)
    
    if client.logged_in:
        nom_utilisateur = client.info.name 
        print(f'Connecté en tant que {nom_utilisateur}')
        today = datetime.date.today()
        global homework
        homework = client.homework(today)

        # Supprimer le message du bot avant d'envoyer le message de connexion
        await interaction.message.delete()
        await interaction.channel.send(content=f"Connexion au pronote de {nom_utilisateur} effectuée.")
    else:
        await interaction.channel.send(content="Échec de la connexion à pronote.")



@bot.tree.command(name="devoirs", description="Donne les devoirs a faire dans la semaine.")
async def devoirs(interaction : discord.Interaction):
    for hw in homework:
        await interaction.response.send_message(f"({hw.subject.name}): {hw.description}")


if __name__ == '__main__':
    bot.run('tu vas bien ?')


