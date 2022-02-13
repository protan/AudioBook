from gtts import gTTS as gt
import sys
if len(sys.argv) > 1 :
    text = sys.argv[1]
    if str(text) =="F" or str(text)=="f" or str(text) =="-F" or str(text)=="-f" :
        file_text =""
        with open(sys.argv[2],'r') as f:
            line = (f.readlines())
        for l in line:
            file_text+=(str(l.replace("\n"," ")))
        name = (file_text.split(" ")[0:3])
        filename =""
        for i in name:
            filename+=str(i)+" "
        audio=gt(str(file_text))
        audio.save(f"{str(filename)}.mp3")
    else:
        filename = (text.split(" ")[0:3])
        name =""
        for i in filename:
            name+=str(i)+" "
        audio=gt(str(text))
        audio.save(f"{str(name)}.mp3")
else:
    print("The AudioBook Python App Build by Protan Halder \nFB    >> https://www.facebook.com/i.am.protan\nEmail >> protanhalder2021@gmail.com\n")
    print('''Command Example\npython3 main.py -F filename.txt\n\tor\npython3 main.py "Here Is you Text"''')

