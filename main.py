import discord
from discord.ext import commands
from prsaw import RandomStuff


api_key = str(input("Api key: "))
channel_id = int(input("Channel id: "))
bot_token = str(input("BOT token: "))

bot = commands.Bot(command_prefix="C")
rs = RandomStuff(async_mode=True, api_key = api_key)



def merge_dicts(l):
  if len(l) == 1:
    return l[0]
  return {**l[0], **merge_dicts(l[1:])}

@bot.event
async def on_ready():
    print("Chat BOT is online")

 
@bot.event
async def on_message(message):
    if bot.user == message.author:
        return

    if message.channel.id ==channel_id:

         r = await rs.get_ai_response(message.content)
         response = merge_dicts(r)
         await message.reply(response['message'])
         await bot.process.commands(message)
         

bot.run(bot_token)

