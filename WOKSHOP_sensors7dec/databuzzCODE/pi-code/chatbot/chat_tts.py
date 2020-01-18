#make sure aux cable is connected and amplified
#Make sure 015 module temp/humid is connected in gpio pin 23
from gtts import gTTS
from rivescript import RiveScript
from pygame import mixer

mixer.init()
rs = RiveScript()
rs.load_directory("./brain")
rs.sort_replies()

while True:
    msg = raw_input("You> ")
    if msg == '/quit':
        quit()
    reply = rs.reply("localuser", msg)
    tts = gTTS(text=reply, lang='en')
    tts.save("data/hello.mp3")
    mixer.music.load("data/hello.mp3") # you may use .mp3 but support is limited
    mixer.music.play()
    print "Bot>", reply




