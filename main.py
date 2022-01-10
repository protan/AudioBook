from gtts import gTTS as gt
import sys
text = sys.argv[1]
if str(text) =="F" or str(text)=="f":
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

