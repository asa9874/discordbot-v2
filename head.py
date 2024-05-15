import discord
from discord.ext import commands
import csv
import time
import random
import requests
from steam import Steam
import math
import asyncio
import json
import datetime
from datetime import datetime as dt
import pprint
from table2ascii import table2ascii as t2a, PresetStyle



intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#진짜
TOKEN_real='디스코드 봇키를 넣어주세요'
#테스트
TOKEN_test='테스트용으로 작동시킬 디스코드 봇키를 넣어주세요'

a=input("실제:r 테스트:t")
if a== 'r': TOKEN=TOKEN_real
else:TOKEN=TOKEN_test