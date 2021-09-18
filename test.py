from janome.tokenizer import Tokenizer
 
path = './test.txt' #同じディレクトリにtext.txtを配置
file = open(path, encoding="utf-8")  #ファイルをオープン Windows or Mac
#file = open(path)  #ファイルをオープン Mac
bindata = file.read()#開いたファイルの読み込み
#textdata = bindata.decode('shift_jis')
 
t = Tokenizer() #形態素解析
dic = {} #辞書
#---------------------------------------------------------------------------------------------
lines = bindata.split("\r\n") #改行で分割                              手順1
#---------------------------------------------------------------------------------------------
for line in lines:  #分割された文章毎に繰り返す
#-----------------------------------------------------------------------------
    malist = t.tokenize(line)  #形態素のリスト
    for w in malist:  # リストの各要素を取り出してカウント
        word = w.surface  #                                          手順2         手順4
        part = w.part_of_speech  #品詞
        if part.find('名詞') &lt; 0: continue
#-----------------------------------------------------------------------------
        if not word in dic:
            dic[word] = 0  #数を格納するカウンター用の変数を生成  #        手順3
            dic[word] += 1  # カウンターを増やす
#---------------------------------------------------------------------------------------------
dic = sorted(dic.items(),key = lambda x:x[1], reverse=True)  #       手順5
#---------------------------------------------------------------------------------------------
for word, cnt in keys[:20]:
    print("{0}({1})\n".format(word,cnt), end="")
