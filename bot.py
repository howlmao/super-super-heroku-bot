import discord
import youtube_dl
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Hello Habibi!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} left the server!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')

@client.command()
@commands.has_role('Staff')
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_role('Staff')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_role('Staff')
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"{ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.ban(reason=reason)

@client.command()
@commands.has_role('Staff')
async def unban(ctx, *, member):

    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned the user.')
        return

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Currently in alpha'))
    print('Bot is working correctly.')

@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

client.login('process.env.BOT_TOKEN');
