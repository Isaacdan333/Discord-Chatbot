import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message) 
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    token = ############ TOKEN BOT IS INPUTTED HERE!###############
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_member_join(member):
        mojo_channel = client.get_channel(696543569795612716)
        await mojo_channel.send("Welcome to the Server!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{channel} said: "{user_message}" ({channel})')
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        
    
    client.run(token)

