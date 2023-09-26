import opencc
import sys

filename=""
while filename!="q":
    try:
        if len(sys.argv)==1:
            filename=input("请拖入文件，输入q退出").replace("\"","").replace("\\","/")
            with open(filename,"r",encoding='utf-8') as f:
                data=f.read()
            converter=opencc.OpenCC("t2s.json")
            result=converter.convert(data)
            with open(filename,"w",encoding='utf-8') as f:
                f.write(result)
            print(result)
            print("- - -转换完成- - -")
        elif len(sys.argv)>1:
            filenames = sys.argv[1:]
            for filename in filenames:
                with open(filename,"r",encoding='utf-8') as f:
                    data=f.read()
                converter=opencc.OpenCC("t2s.json")
                result=converter.convert(data)
                with open(filename,"w",encoding='utf-8') as f:
                    f.write(result)
                print(result)
                input("- - -转换完成- - -")
                filename="q"
    except:
        pass