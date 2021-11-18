import discord
import discord
import discord.utils
from discord.utils import *
import discord.channel
from discord.channel import *
from discord import *
from discord.ext import *
from discord.ext.tasks import *
from discord.ext import tasks, commands
import discord.user
from discord.user import *
import discord.file
from discord.file import *
import datetime
import codecs
import os
from os import *
#De bot initialiseren
key = os.getenv("API_KEY")
webhookn = os.getenv("WEBHOOK_KEY")
webhookl = os.getenv("WEBHOOK_SECRET")
bot = commands.Bot(command_prefix="~")
#Webhook link als je dat wilt moet je naar channel instellingen en dan integraties webhooks en dan nieuwe webhook en doe je webhooklink kopiëren
webhookb = Webhook.partial(webhookn, webhookl, adapter=RequestsWebhookAdapter())
#De loop
henk = 0
@tasks.loop(hours=24)
async def spammer():
    global henk
    henk += 1
    print("hallo ik heb gerunt")
    if henk >= 2:
        #Bij dat <@> ding moet aidans discord id daartussen zodat die gepingt word en je kan ook nog de username aanpassen
        webhookb.send("<@598830640401612819> Je vader is kaal", username="Aidan zijn kale vader", file=File("kaal.png"), avatar_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.q7TeO3C2vDN_INY3Rb67VAHaEK%26pid%3DApi&f=1")
    else:
        return
#Loop starten en de bot starten
spammer.start()
bot.run(key)