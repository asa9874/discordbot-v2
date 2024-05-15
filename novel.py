from head import *

#정의
Novel_list=[]  

#소설
class Novel:

    def __init__ (self,title,auther,tag,view,episode,recommend,perview,url):
        self.title=title
        self.view=view
        self.recommend=recommend
        self.episode=episode
        self.auther=auther
        self.tag=tag
        self.perview=perview
        self.url=url
#엑셀읽기
def readcsv_novel():
    f=open('data.csv','rt',encoding="CP949")
    rdr = csv.reader(f)

    for line in rdr:
        novel=Novel(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        Novel_list.append(novel)

#실제부분   
readcsv_novel()

#디코봇
@bot.command(aliases=['노벨'])
async def 소설(ctx):
    novel=random.choice(Novel_list)
    
    embed = discord.Embed(title =novel.title + "  (작가:"+novel.auther+")", description = "", color = 0x62c1cc)
    embed.add_field(name ="조회수:"+novel.view +"  추천:"+novel.recommend, value = "편당조회수:"+novel.perview,inline=False)
    embed.add_field(name ="태그", value = novel.tag,inline=False)
    embed.add_field(name ="주소", value = novel.url,inline=False)
    embed.set_thumbnail(url="https://images.crunchbase.com/image/upload/c_pad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/gzkbdivqqdslfu8qgrc3")
    await ctx.send(embed = embed)


