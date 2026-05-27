import discord
from discord.ext import commands

# === CONFIGURE THESE ===
TOKEN = "MTUwOTMxNDQ0MTE0NDA0NTc0MA.GWGEAm.0iQpI8H-LR2-uT8UQyH1fF7-rIkq9h4YaPqMF4"

WELCOME_CHANNEL_ID = 1401374600700629082  # welcome channel ID
GOODBYE_CHANNEL_ID = 1509314470428541121  # goodbye channel ID

GTE_EMOJI_ID = 1431630714196984031        # your logo emoji ID
# =======================

intents = discord.Intents.default()
intents.members = True  # needed for join/leave events

bot = commands.Bot(command_prefix="!", intents=intents)

def get_gte_emoji(guild: discord.Guild):
    return discord.utils.get(guild.emojis, id=GTE_EMOJI_ID)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_join(member: discord.Member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        return

    msg = await channel.send(
        f"Hello {member.mention} and welcome to TGG | The Golden Gorillas!*"
    )

    emoji = get_gte_emoji(member.guild)
    if emoji:
        try:
            await msg.add_reaction(emoji)
        except discord.HTTPException as e:
            print(f"Failed to add welcome reaction: {e}")

@bot.event
async def on_member_remove(member: discord.Member):
    channel = member.guild.get_channel(GOODBYE_CHANNEL_ID)
    if channel is None:
        return

    msg = await channel.send(
        f"{member.mention} Thank you for joining the TGG server We hope to see you again soon.👋"
    )

    emoji = get_gte_emoji(member.guild)
    if emoji:
        try:
            await msg.add_reaction(emoji)
        except discord.HTTPException as e:
            print(f"Failed to add goodbye reaction: {e}")

bot.run(TOKEN