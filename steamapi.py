from head import *

#스팀 api 설정
steam = Steam("steam_api_key_here!")



#게임이름, 게임가격 리턴해주는 함수
def nameprice_check(i):
    name=i["name"]

    try:#유료
        
        price=steam.apps.search_games(name)["apps"][0]["price"]
        if (price[0] != '$'):
            price=0
        else:
            price=float(price[1:])*1000
    except:#무료 
        price=0

    return name,price

#게임 가격 합산
def pricesum(price_list):
    sumprice=0
    for i in price_list:
        sumprice=sumprice+i

    return sumprice


#스팀
@bot.command()
async def 스팀(ctx,*,steamid):
    await ctx.send(f'잠시만기다려주세여~')
    #아이디 입력받아 식별코드 얻기
    try:#아이디
        ID=steam.users.search_user(steamid)["player"]["steamid"]
        #게임목록 추출(리스트)
        game=steam.users.get_owned_games(ID)["games"]
    except:
        try:#고유코드
            game=steam.users.get_owned_games(steamid)["games"]
        except:
            try:#프로필주소
                game=steam.users.get_owned_games(steamid[36:-1])["games"]
            except:
                await ctx.send(f'실패')
    

    
    #게임가격리스트,게임수
    game_price_list=[]
    gamenum=0
    embed = discord.Embed(title = "스팀", description = "", color = 0x62c1cc)
    for i in game:
        print(str(gamenum)+"시작")
        gamenum=gamenum + 1
        game_name,game_price=nameprice_check(i)
        game_price_list.append(game_price)
    gamesum=pricesum(game_price_list)
    
    embed = discord.Embed(title = "당신이 땅에다 버린돈", description = "", color = 0x62c1cc)
    embed.add_field(name =  "게임수:"+str(gamenum), value ="버린돈은 아마도"+str(gamesum)+"원",inline=False)
    embed.set_thumbnail(url="https://t3.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/6Hj8/image/I97Vf9b84uTpJ3rmYebSPcIGRho.jpg")
    await ctx.send(embed = embed)