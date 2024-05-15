from head import *

headers_chzzk= {'User-Agent': 'Mozilla/5.0'} 
user_chzz='방송확인할 방송인 코드를 적어주세요~'
url_chzz='https://api.chzzk.naver.com/service/v1/channels/'+user_chzz

stoking_do=False #방송라이브 확인 여부확인
#방송확인
@bot.command(aliases=['방송'])
async def 방송확인(ctx,*,do):
    global stoking_do
    if do=='ON': 
        stoking_do =True
        await ctx.send("방송확인중")
    elif do=='OFF': 
        stoking_do =False
        await ctx.send("방송확인끝")
    else: await ctx.send("그게 뭐임")
    last_check=0
    check=0
    while stoking_do:
        r= requests.get(url_chzz,headers=headers_chzzk)
        if(r.json()['content']['openLive'] == True): 
            check=1
            print("뱅온")
        else: 
            check=0
            print("뱅오프")

        if check != last_check:
            if check == 0: await ctx.send("뱅오프~"+"https://chzzk.naver.com/live/"+user_chzz)
            else: await ctx.send("뱅온"+"https://chzzk.naver.com/live/"+user_chzz)
        last_check=check
        await asyncio.sleep(3)