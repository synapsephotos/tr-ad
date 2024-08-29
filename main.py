import discord
from keep_alive import keep_alive
import asyncio

TOKEN = process.env.Authorization
CHANNEL_ID = "1245731705113940089"
MESSAGE = "🌙 __The Revengeance__ | NA Clan 🇺🇸\n- Requirements:  Follow the upgrade requirements for the week, have 1k+ wins or 50k+ RAP\n- Stats: Coin Earning - **MAX** | Welfare - **MAX** | Luck - **FIVE** | Size **FIVE** | 3 upgrades away from Quantum Arena. 👾 \nDM <@992221688362192956> to apply! ^^"

client = discond.Client()

@client.event
async def on_ready():
  channel = client.get_channel(CHANNEL_ID)
  while True:
    await channel.send(MESSAGE)
    await asyncio.sleep(22 * 60)

client.run(TOKEN)
