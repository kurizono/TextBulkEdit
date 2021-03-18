import shutil
from glob import glob
import pathlib
import codecs

#入力テキストと出力テキストのファイルのパス
inputfile = './input'
outputfile = './output'
#変更テキスト(設定テキスト)のパス
changewordpath = './setting/change.txt'

#ファイルの変更処理
for inputtext in pathlib.Path(inputfile).glob('*.txt'):
  #inputファイル読み込み
  with open(inputtext, 'r', encoding='UTF-8') as f:
    inputdata = f.read()
  outputtext = outputfile + '/' + inputtext.name
  outputdata = inputdata
  #ワード書き換え
  with open(changewordpath, 'r',  encoding='utf-8') as f:
    for line in f:
      changewords = line.split(",")
      print(line)
      outputdata = outputdata.replace(changewords[0], changewords[1])
  codecs.open
  
  with codecs.open(outputtext, 'w','cp932', 'ignore') as f:
    print(outputdata, file=f)

