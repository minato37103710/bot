import discord
from discord.ext import commands
import os, re, json, random
from janome.tokenizer import Tokenizer




dict_file = "chatbot-data.json"
tokenizer = Tokenizer()

if os.path.exists(dict_file):
    di = json.load(open(dict_file, "r"))

def register_dic(words):
    global di
    if list(words) == 0: return
    tmp = ["@"]
    for i in words:
        print(i)
        word = i.surface
        print(word)
        if word == "" or word == "\r\n" or word == "\n": 
            print('ok')
            continue
        tmp.append(word)
        if len(tmp) < 3: 
            print('ok')
            continue
        if len(tmp) > 3: 
            tmp = tmp[1:]
            print(tmp)
        set_word3(di, tmp)
        if word == "。" or word == "?":
            tmp = ["@"]
            continue
        #辞書更新毎にファイル保存
    with open(dict_file, "w", encoding="utf-8") as f:
      json.dump(di, f)   
 

def set_word3(di, s3):
    w1, w2, w3 = s3
    if not w1 in di: di[w1] = {}
    if not w2 in di[w1]: di[w1][w2] = {}
    if not w3 in di[w1][w2]: di[w1][w2][w3] = 0
    di[w1][w2][w3] += 1


def make_sentence(head):
    ret = []
    if head not in di: return ""
    top = di[head]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        if w1 in di and w2 in di[w1]:
            w3 = word_choice(di[w1][w2])
        else:
            w3 = ""
        ret.append(w3)
        if w3 == "。" or w3 == "？" or w3 == "": break
        w1, w2 = w2, w3
    return "".join(ret)


def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))



# botに返答させる
def make_reply(text):
    # まず単語を学習する
    if text[-1] != "。": text += "。"
    words = tokenizer.tokenize(text)
    register_dic(words)
    # 辞書に単語があれば、そこから話す
    for w in words:
        face = w.surface
        ps = w.part_of_speech.split(',')[0]
        if ps == "感動詞":
            return face + "。"
        if ps == "名詞" or ps == "形容詞":
            if face in dic: return make_sentence(face)
    return make_sentence("@")

#ここからメッセージ取得&返信

#
#
#以下、discord処理
#
#

bot = commannds.Bot(command_prefix='jt!',intents=discord.Intents.all())



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')




@bot.event

async def on_message(message):
    if not message.channel.id==884383014199656448:
        return

    if message.attachments:
        pass
    
    if message.author.bot:
        return
    
    if message:    
        text = message.content
        res = make_reply(text)
        if not res:
            return
        else:
            await message.channel.send(res)


client.run(os.getenv('token'))
