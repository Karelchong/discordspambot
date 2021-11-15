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
import asyncio
import datetime
import codecs
#De bot initialiseren
omelet = "BGN5BQD1AQD1ZmLkZGD3BGp1.LMXAzt.X_psm5uWR2hxUToRZE--ZX0hqgt"
gebakkenei = lambda s : codecs.getencoder("rot-13")(s)[0]
bot = commands.Bot(command_prefix="~")
#Webhook link als je dat wilt moet je naar channel instellingen en dan integraties webhooks en dan nieuwe webhook en doe je webhooklink kopiëren
#https://discord.com/api/webhooks/816724608655949834/KIeJHhtP-XAwJ6n-e1f6mEkkWhFfD14mpdnAkLPSIvQqmzN-5g2GF0J2cL9VDlXInXWu bottest webhook
#https://discord.com/api/webhooks/909838462910365716/JfkW2URY-44ZzbsCGqMXv4NfwPivC7VsEI8eD4EHLczWq7P4pU3db48gEjL7WhMlzpo2 maarten webhook
#https://discord.com/api/webhooks/909844723404009532/tHkR-cZDlCG6y2VhnlDQX8VF22X0d3ZYhJ4FVlSFAV5fvt4jx5FOoSRFEbjgXxTefA1s andere bottest webhook
#Als je zo'n link hebt moet het nummer ding hier en het ding na de slash met alle random cijfers en letters hier
#webhookb = Webhook.partial(909838462910365716, 'JfkW2URY-44ZzbsCGqMXv4NfwPivC7VsEI8eD4EHLczWq7P4pU3db48gEjL7WhMlzpo2', adapter=RequestsWebhookAdapter())
webhookb = Webhook.partial(909844723404009532, 'tHkR-cZDlCG6y2VhnlDQX8VF22X0d3ZYhJ4FVlSFAV5fvt4jx5FOoSRFEbjgXxTefA1s', adapter=RequestsWebhookAdapter())
#De loop
@tasks.loop(hours=24)
async def spammer():

    #Bij dat <@> ding moet aidans discord id daartussen zodat die gepingt word en je kan ook nog de username aanpassen
    webhookb.send("<@598830640401612819> Je vader is kaal", username="Aidan zijn kale vader", file=File("kaal.png"), avatar_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.q7TeO3C2vDN_INY3Rb67VAHaEK%26pid%3DApi&f=1")
#Loop starten en de bot starten
spammer.start()
bot.run(gebakkenei(omelet))