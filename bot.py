import discord, asyncio, os, traceback
from gtts import gTTS
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), owner_ids=[730281216678297660])
bot.remove_command('help')

@bot.event
async def on_ready():
    print("bot is ready!")

@bot.command(name="접속", aliases=['connect'])
async def connect(ctx):
    voice = ctx.author.voice
    if not voice:
        await ctx.reply(f"❎ {ctx.author.mention}, 음성 채널에 접속 후 명령어를 사용하세요!")
    else:
        vc = await voice.channel.connect()
        await ctx.reply(f"✅ {ctx.author.mention}, 음성 채널에 봇이 들어왔어요!")
        await discord.voiceState.self_mute(True)

@bot.command(name="tts")
async def tts(ctx, *, text):
    tts = gTTS(text=text, lang="ko")
    tts.save("text.mp3")
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc:
        vc = await ctx.author.voice.channel.connect()
        await ctx.reply(f"✅ {ctx.author.mention}, 음성 채널에 봇이 들어왔어요!")
        await discord.voiceState.self_mute(True)
    
    vc.play(discord.FFmpegPCMAudio('text.mp3'), after=None)
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 5
    await ctx.message.add_reaction('✅')

bot.run("token here!")