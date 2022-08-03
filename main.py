# discord.py version : https://github.com/Rapptz/discord.py@13c725f1836168eca97a5e51180625a32f3eb2cc (Development)
from random import shuffle
import discord
from discord import app_commands

# import discord bot token file
import apikeys

charList = ["a", "b", "c", "d", "e", "f",
			"g", "h", "i", "j", "k", "l",
			"m", "n", "o", "p", "q", "r",
			"s", "t", "u", "v", "w", "x",
			"y", "z", "A", "B", "C", "D",
			"E", "F", "G", "H", "I", "J",
			"K", "L", "M", "N", "O", "P",
			"Q", "R", "S", "T", "U", "V",
			"W", "X", "Y", "Z", "0", "1",
			"2", "3", "4", "5", "6", "7",
			"8", "9"
]

def base62(n):
	result = []
	while n > 0:
		n, mod = divmod(n, 62)
		result.append(mod)
	return result[::-1]

class Client(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.default())
		self.synced = False
	
	async def on_ready(self):
		await self.wait_until_ready()
		if not self.synced:
			await tree.sync()
			self.synced = True

client = Client()
tree = app_commands.CommandTree(client)

@tree.command(
	name="randnick",
	description="명령어를 사용한 사람의 이름을 임의로 변경합니다.",
)
async def self(interaction: discord.Interaction):
	if interaction.guild:
		shuffle(charList)
		randName = ""
		for i in base62(interaction.user.id):
			randName += charList[i]
		await interaction.response.send_message(f"유저 {interaction.user.name}님의 닉네임을 {randName}으로 변경하였습니다.")
		await interaction.user.edit(nick=randName)
		# interaction.send_message(f"이 채널에서는 사용할 수 없는 기능입니다.")

client.run(apikeys.BOTTOKEN)
