import opencc
import sys
import re

if len(sys.argv)==1:
    filenames=input("请拖入文件").replace("\\","/")
    filenames=re.findall(r'(?<=").*?(?=")',filenames)
    filenames.remove(" ")
elif len(sys.argv)>1:
    filenames = sys.argv[1:]
for filename in filenames:
    with open(filename,"r",encoding='utf-8') as f:
        data=f.read()
    converter=opencc.OpenCC("t2s.json")
    result=converter.convert(data)
    with open(filename,"w",encoding='utf-8') as f:
        f.write(result)
        print(filename)
input("- - -转换完成- - -")