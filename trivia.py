import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix= ";")  # You can change prefix like that "/","$" e.t.c..
client.remove_command("help")

@client.event()
async def on_ready():
    print("logged in as:" + client.user.name)
    print("--------")
    print("Made By LATENT MAN#9088")


@client.command()
@commands.has_permissions(manage_messages=True)   # you can change the permission like that "administrator" e.t.c..
async def accuracy(ctx, game=None,time=None,accuracy=None,ques=None,prize=None,status=None):
    embed=discord.Embed(title="Result Of Games", description="", color=0xfffff)
    embed.add_field(name="Game", value=game)
    embed.add_field(name="Time", value=time)
    embed.add_field(name="Accuracy", value=accuracy)
    embed.add_field(name="Question", value=ques)
    embed.add_field(name="Prize", value=prize)
    embed.add_field(name="Game Status:", value=status)
    embed.set_thumbnail(url="PUT YOUR THUMBNAIL (IMAGE OF GAME)")
    embed.set_footer(text=f"Made By LATENT MAN#9088", icon_url="") #Change Footer And Icon url
    await ctx.send(content="@everyone", embed=embed)


@client.command()
async def alert(ctx, game=None,time=None,prize=None):
    if not game or not time or not prize:
        embed=discord.Embed(
            title="Wrong Use!",
            description="Please Check, The Word, Use ex `?alert hq 6:30 5000$`",
            color= 0xfffff
            )
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Game Alert!", description=f"{game} Time. \nTime:- {time} \nPrize Pool:- {prize} \n\n Ready Guys Connect In Voice And Get Best Answer!!.", color=0xfffff)
        embed.set_thumbnail(url="PUT YOUR THUMBNAIL")
        embed.set_footer(text=f"Made By LATENT MAN#9088", icon_url="") # Change Footer And Icon url.
        await ctx.send(content="@everyone", embed=embed)

@client.command()
async def q(ctx, question: str):
    if not question:
        embed=discord.Embed(
            title="Wrong Use!",
            description="Please Use, `;q1`, `;q 1`",
            color=0xfffff
            )
    else:
        embed=discord.Embed(title="Your Server Name", description=f"**Question No. {question} is Coming Your Mobile 📱 Screen., Please React Below.**", color=0xfffff)
        embed.set_thumbnail(url="") # Server (image) here
        embed.set_footer(text=f"Made By LATENT MAN#90888", icon_url="") # Change Footer And Icon url.
        await ctx.send(content="@everyone", embed=embed)




# Accuracy Command = ";accuracy loco 7pm 10/10 10 49rs All_won"
# Alert Command = ";alert loco 7pm 15000rs"
# question = ";q1"

client.run("Token Here")
