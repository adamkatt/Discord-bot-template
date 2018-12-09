#id: 
#Token:
#PERMISSIONS INTEGER: 
#https://discordapp.com/oauth2/authorize?&client_id=YOURID&scope=bot&permissions=YOURPERMISSIONS
import discord
client = discord.Client()
@client.event 
async def on_ready():
    print (f'we have logged in as {client}')
@client.event


async def on_message(message):
    print(f"{message.channel}:{message.author}:{message.author.name}:{message.content}")#print the message and relevant information
    
    ##
    if message.content[0:3] == '.m ':
        
        print ('ok')
        comment = message.content.replace('.m ','')
        await client.send_message(message.channel,comment)#you must define the channel as your first parameter always, and the actual comment as your second
    ##
    #between the '##' is where the bulk of your program should go


client.run("YOUR TOKEN")
