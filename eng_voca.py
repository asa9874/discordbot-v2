from head import *

#------정의
Voca_list=[]  
Voca_print_num=15


#--------함수부분
#단어 클래스
class VOCA:
    voca_num=0
    def __init__(self,id,en,kor):
        self.id=id
        self.en=en
        self.kor=kor
        VOCA.voca_num=VOCA.voca_num+1

#엑셀파일 읽기
def readcsv_voca():
    f=open('english.csv','rt',encoding="CP949")
    rdr = csv.reader(f)

    for line in rdr:
        e=VOCA(line[0],line[1],line[2])
        Voca_list.append(e)

#무작위 단어장 생성
def rand_voca():
    list_rand=random.sample(Voca_list,Voca_print_num)
    return list_rand

#단어장 순서대로
def voca_note(num):
    list_note=[]
    start_num=(num-1)*Voca_print_num
    end_num=num*Voca_print_num
    if (num*Voca_print_num)>VOCA.voca_num: end_num=VOCA.voca_num

    for i in range(start_num,end_num,1):
        list_note.append(Voca_list[i])
    return list_note

#---------실제부분
readcsv_voca()
Voca_page=math.ceil(VOCA.voca_num/Voca_print_num)


#--------디코봇 명령어----------
#무작위
@bot.command(aliases=['단어'])
async def 무작위영어(ctx):
    text1=""
    for i in rand_voca():
        text1=text1+i.kor+":"+i.en+"\n"

    await ctx.send(text1)

#단어장
@bot.command(aliases=['영어'])
async def 영단어(ctx,*,number):
    if (int(number)>=Voca_page): await ctx.send(str(VOCA.voca_num)+str(Voca_print_num)+str(Voca_page)+"없다")
    else:
        text1="영단어<<("+number+"/"+str(Voca_page)+">>)\n"
        for i in voca_note(int(number)):
            text1=text1+i.id+"."+i.kor+":"+i.en+"\n"

        await ctx.send(text1)