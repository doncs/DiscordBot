import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = ".")
status = cycle(['Doncs is cool', 'Doncs1 #1', 'Kevv gay'])

@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready.")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    print(f'Welcome to the server, (member)!')

@client.event
async def on_member_remove(member):
    print(f'(member) has caught ligma')

@client.command()
async def ping(ctx):
    await ctx.send(f'YEET! {round(client.latency * 1000)}ms')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Replay hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it",
                 'My reply is no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 'Yes, proxi is gay.',
                 'Yes, proxi is gay!']
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')



@client.command()
async def remove(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} has been unbanned')
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def commands(ctx):
    await ctx.send('List of commands: .ping, .8ball, .remove, .kick, .ban, .unban, .commands')




client.run('Njk0MzYwNzc3NDY0NzQxOTgw.XoLNRg.lorY-NkJrjzbgceMwTwscGyeE4g')