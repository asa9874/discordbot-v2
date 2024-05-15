from head import *


#인사
@bot.command(aliases=['하이','반가워','ㅎㅇ','안녕'])
async def 인사(ctx):
    embed = discord.Embed(title = "안녕", description = "", color = 0x62c1cc)
    await ctx.send(embed = embed)


#명령어 모음
@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title ="!인사" ,description = "", color = 0x62c1cc)
    embed.add_field(name ="!소설" ,value = "",inline=False)
    embed.add_field(name ="!스팀 <프로필코드>" ,value = "",inline=False)
    embed.add_field(name ="!영단어 <번호>" ,value = "",inline=False)
    embed.add_field(name ="!무작위영어" ,value = "",inline=False)
    embed.set_thumbnail(url="https://images.crunchbase.com/image/upload/c_pad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/gzkbdivqqdslfu8qgrc3")
    await ctx.send(embed = embed)