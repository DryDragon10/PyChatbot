#imports
import discord
from discord.ext import commands
from prsaw import RandomStuff


api_key = str(input("Api key: "))
#intro
bot = commands.Bot(command_prefix="C")
rs = RandomStuff(async_mode =True, api_key=api_key)


#inputs
api_key = str(input("Api key: "))
channel_id = int(input("ID of the channel u want the bot to talk:"))
TOKEN = str(input("Bot TOKEN:"))


#when bot is online
@bot.event
async def on_ready():
    print("Chat BOT is online")

#main 
@bot.event
async def on_message(message):
	if bot.user == message.author:
		return

	if message.channel.id == channel_id:
	 	response = await rs.get_ai_response(message.content)
	 	await message.reply(response)
	 	await bot.process.commands(message)
	 	

bot.run(TOKEN)
