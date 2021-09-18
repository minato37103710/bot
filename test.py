from janome.analyzer import Analyzer
from janome.tokenizer import Tokenizer
from janome.tokenfilter import POSKeepFilter

text = '蛇の目はPure Ｐｙｔｈｏｎな形態素解析器です。'
tokenizer = Tokenizer()
token_filters = [POSKeepFilter(['名詞'])]
a = Analyzer([], tokenizer, token_filters)

for token in a.analyze(text):
  print(token)
