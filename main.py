import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Required to access members
intents.message_content = True  # Required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def dm(ctx, *, message):
    if ctx.author.guild_permissions.administrator:
        await ctx.send("🚀 Sending DMs...")
        for member in ctx.guild.members:
            if not member.bot:
                try:
                    await member.send(message)
                except:
                    print(f"❌ Could not send to: {member.name}")
        await ctx.send("✅ All messages sent.")
    else:
        await ctx.send("❌ You must be an admin to use this command.")

bot.run("MTM4OTkyMTk4NTI3MzkyNTY5Ng.GAPQi9.BQ0yfw0FxRXX9c7KNOicUEwxNXQN1fI48VOEBM")
