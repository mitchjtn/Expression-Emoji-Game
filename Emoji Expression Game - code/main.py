import tkinter as tk
import time as tm
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
import random
from deepface import DeepFace  #age, gender, emotion face recognition
import cv2
from datetime import datetime
import time
import threading

window = Tk()
window.geometry("700x640")
window.title("Emoji Expression Game")

def play():
    mixer.music.play()

def mute():
    mixer.music.stop()

state=0
def SwitchSoundButton(event):
    global state
    if state==1:
        soundButton.config(image=ButOff, command = play)
        state=0
    else:
        soundButton.config(image=ButOn, command = mute)
        state=1

def raise_frame(frame):
    frame.tkraise()

def close_window():
    window.destroy()

def tick_time():
    global timenow
    newtime = tm.strftime('%d/%m/%Y %H : %M : %S ')
    if newtime != timenow:
        timenow = newtime
        clock.config(text=timenow)
    clock.after(200, tick_time)

def loading():
    loadingText.config(text = "Please Wait for the game ...")

def play_music():
    mixer.init()
    mixer.music.load("Media/cobain.mp3")
    mixer.music.play(loops = 500)

#----------------------

#FRAME LIST

#Main Menu
menu = Frame(window)
menu.place(x = 0, y = 0, width = 700, height = 640)

#How to Play
htp = Frame(window)
htp.place(x = 0, y = 0, width = 700, height = 640)

#Rule 1st Game
rules11 = Frame(window)
rules11.place(x = 0, y = 0, width = 700, height = 640)
rules12 = Frame(window)
rules12.place(x = 0, y = 0, width = 700, height = 640)
rules13 = Frame(window)
rules13.place(x = 0, y = 0, width = 700, height = 640)
rules14 = Frame(window)
rules14.place(x = 0, y = 0, width = 700, height = 640)
rules15 = Frame(window)
rules15.place(x = 0, y = 0, width = 700, height = 640)

#Rule 2nd Game
rules21 = Frame(window)
rules21.place(x = 0, y = 0, width = 700, height = 640)
rules22 = Frame(window)
rules22.place(x = 0, y = 0, width = 700, height = 640)
rules23 = Frame(window)
rules23.place(x = 0, y = 0, width = 700, height = 640)
rules24 = Frame(window)
rules24.place(x = 0, y = 0, width = 700, height = 640)

#Game
openCamera1 = Frame(window)
openCamera1.place(x = 0, y = 0, width = 700, height = 640)
openCamera2 = Frame(window)
openCamera2.place(x = 0, y = 0, width = 700, height = 600)


#Opening
opening = Frame(window)
opening.place(x = 0, y = 0, width = 700, height = 640)

#Result
resultFrame = Frame(window)
resultFrame.place(x = 0, y = 0, width = 700, height = 640)

raise_frame(opening)
#----------------------

#FONT LIST

fontStyle1 = tkFont.Font(family = "KG Party on the Rooftop", size = 45) #Main Menu - Title
fontStyle2 = tkFont.Font(family = "Hobo Std", size = 20) #Main Menu - Subtitle
fontStyle3 = tkFont.Font(family = "Orange Juice", size = 40) #Main Menu & Rules Menu - Choose Game Button Number
fontStyle4 = tkFont.Font(family = "Hobo Std", size = 25) #Main Menu & Rules Menu - Choose Game Button Text
fontStyle5 = tkFont.Font(family = "Times New Roman", size = 17) #Main Menu - Loading
fontStyle6 = tkFont.Font(family = "Fipps", size = 25) #How To Play - Title
fontStyle7 = tkFont.Font(family = "Pretty Neat", size = 12) #How To Play - Subtitle
fontStyle8 = tkFont.Font(family = "Times New Roman", size = 13) #Opening - Time
fontStyle9 = tkFont.Font(family = "Times New Roman", size = 12) #Opening - Button
fontStyle10 = tkFont.Font(family = "Time New Roman", size = 15) #Main Menu - Rules
fontStyle11 = tkFont.Font(family = "Keep On Truckin", size = 17) #Open Camera - Emoji Name
fontStyle12 = tkFont.Font(family = "Keep On Truckin", size = 50) #Open Camera - Lives Counter
fontStyle13 = tkFont.Font(family = "Keep On Truckin", size = 30) #Open Camera - Title
fontStyle14 = tkFont.Font(family = "Times New Roman", size = 18)
fontStyle15 = tkFont.Font(family = "Keep On Truckin", size = 17)
fontStyle16 = tkFont.Font(family = "Keep On Truckin", size = 40)
fontStyle17 = tkFont.Font(family="Orange Juice", size=40) #Result
fontStyle18 = tkFont.Font(family="Orange Juice", size=26) #Result
fontStyle19 = tkFont.Font(family="Times New Roman", size = 13) #Result

#----------------------

#OPENING

#BG music
play_music()

#ButtonMusic
ButOn = tk.PhotoImage(file = "Media/on.png")
ButOff = tk.PhotoImage(file = "Media/of.png")
soundButton = tk.Button(cursor = "hand2", image = ButOff, borderwidth = 0, height = 25, width = 25)
soundButton.bind("<Button-1>", SwitchSoundButton)
soundButton.place(x=470, y=9)

#BG Image
openingimg = ImageTk.PhotoImage(Image.open("Media/pembuka2.jpg"))
openingbg = tk.Label(opening, image = openingimg)
openingbg.pack()

#Time & Date
timenow = ' '
cFrame = tk.Frame(width = 200, height = 100, bg = "green")
clock = tk.Label(opening, bg = "#f6c624", text = timenow, font = fontStyle8)
clock.place(x = 510,y = 10)
tick_time()

#Next
butNextOpen = tk.Button(opening, cursor = "hand2", text = "Next", height = 1, width = 5, bg = "#f6c624",
                        font = fontStyle9, command = lambda: raise_frame(menu))
butNextOpen.place(x = 280,y = 570)

#Exit
butExitOpen = tk.Button(opening, cursor = "hand2",text = "Exit", height = 1, width = 5, bg = "#f6c624",
                        font = fontStyle9, command = close_window)
butExitOpen.place(x = 350,y = 570)

#----------------------

#MAINMENU

#Title and Subtitle
menuTitle = tk.Label(menu, text = "                                       Expression Emoji Game                                      ",font = fontStyle1, bg = "#fdd501")
menuTitle.pack()
menuSubTitle = tk.Label(menu, text = "                                                Show your expression !!!                                                ",font = fontStyle2, fg = "#fdd501", bg = "black")
menuSubTitle.pack()

#BG Image
mainmenuimg = ImageTk.PhotoImage(Image.open("Media/latar2.jpg"))
mainmenubg = tk.Label(menu, image = mainmenuimg)
mainmenubg.pack()

#Game 1
imgGame1 = tk.PhotoImage(file = "Media/btu1.png")
butGame1 = tk.Button(menu, cursor = "hand2", image = imgGame1, borderwidth = 0, width = 280, height = 250,
                     bg = "#fdd501", command = lambda : game1_start())
butGame1.place(x = 50,y = 230)
labGame1 = tk.Label(menu, cursor = "hand2", text = "             1", font = fontStyle3, bg = "#fdd501", fg = "black")
labGame1.place(x = 50,y = 210)
textGame1 = tk.Label(menu, text = "Imitate Emoji", font = fontStyle4, bg = "#fdd501", fg = "black")
textGame1.place(x = 80, y = 480)

#Game 2
imgGame2 = tk.PhotoImage(file = "Media/btu2.png")
butGame2 = tk.Button(menu, cursor = "hand2", image = imgGame2, borderwidth = 0, width = 280, height = 250,
                     bg = "#fdd501",command = lambda : game2_start())
butGame2.place(x = 400, y = 230)
labGame2 = tk.Label(menu, cursor = "hand2", text = "              2", font = fontStyle3, bg = "black", fg = "#fdd501")
labGame2.place(x = 400, y = 210)
textGame2 = tk.Label(menu, text = "Show Expression", font = fontStyle4, bg = "black", fg = "#fdd501")
textGame2.place(x = 410, y = 480)

#Loading Text
loadingText = tk.Label(menu, text="", font=fontStyle5, bg="#fdd501", fg = "black")
loadingText.place(x = 230,y = 550)

#Rules
butRules = tk.Button(menu, cursor = "hand2", text = "Rules", height = 1, width = 5, bg= "#fdd501", font = fontStyle10,
                     command = lambda: raise_frame(htp))
butRules.place(x = 540,y = 580)

#Exit
butExit = tk.Button(menu, cursor = "hand2", text = "Exit", height = 1, width = 5, bg="#fdd501", font = fontStyle10,
                    command = close_window)
butExit.place(x = 620,y = 580)

#----------------------

#HOWTOPLAY


#Title and Subtitle
htpTitle = tk.Label(htp, text="                              HOW TO PLAY?                             ", font = fontStyle6, bg = "#fdd501")
htpTitle.pack()
htpSubtitle = tk.Label(htp, text="                                                          Which one do you want to choose?                                                           ", font = fontStyle7, bg = "black", fg = "#fdd501")
htpSubtitle.pack()

#BG Image
htpimg = ImageTk.PhotoImage(Image.open("Media/latar2.jpg"))
htpbg = tk.Label(htp, image = htpimg)
htpbg.pack()

#Game1
imgRules1 = tk.PhotoImage(file = "Media/btu1.png")
butGameRules1 = tk.Button(htp, cursor="hand2", image = imgRules1, borderwidth = 0, width = 280, height = 250,
                          bg="#fdd501", command = lambda: raise_frame(rules11))
butGameRules1.place(x=50,y=240)
labelRules1 = tk.Label(htp, cursor="hand2", text="             1", font=fontStyle3, bg= "#fdd501")
labelRules1.place(x=50,y=220)
my_text1 = tk.Label(htp, text= "Imitate Emoji", font=fontStyle4,bg= "#fdd501", fg="black")
my_text1.place(x=80, y = 490)

#Game2
imgRules2 = tk.PhotoImage(file = "Media/btu2.png")
butGamesRules2 = tk.Button(htp, cursor="hand2", image = imgRules2, borderwidth = 0, width = 280, height = 250,
                           bg="black",  command = lambda: raise_frame(rules21))
butGamesRules2.place(x=400, y=240)
labelRules2 = tk.Label(htp, cursor="hand2", text= "              2",font=fontStyle3, bg="black", fg = "#fdd501")
labelRules2.place(x=400,y=220)
my_text2 = tk.Label(htp, text = "Show Expression", font= fontStyle4, bg="black", fg = "#fdd501")
my_text2.place(x=410, y = 490)

#MainMenu
butBackMenu = tk.Button(htp, cursor = "hand2", text = "Back to Main Menu", bg = "#fdd501",
                        command = lambda: raise_frame(menu))
butBackMenu.place(x = 300, y = 600)

#----------------------

#1STGAMERULES

#Game 1 - Rule 1

#Title and Subtitle
title11 = tk.Label(rules11, text = "                              HOW TO PLAY?                             ",
                   font = fontStyle6, bg = "#fdd501")
title11.pack()
subtitle11 = tk.Label(rules11, text = "                                Emoji to Expression!                               ", font = fontStyle7, bg = "#fdd501")
subtitle11.pack()

#BG Image
rule11img = ImageTk.PhotoImage(Image.open("Media/kuning.jpg"))
rule11bg = tk.Label(rules11, image = rule11img)
rule11bg.pack()

#Rule
rule11 = tk.Label(rules11, text = "1. The game will show an emoji randomly. You need to guess what emoji it is.",
                  bg = "#fdd501")
rule11.place(x = 140, y = 180)

#Button
butRule11r = tk.Button(rules11, cursor = "hand2", text = ">>>", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules12))
butRule11r.place(x = 630, y = 270)


#Game 1 - Rule 2

#Title and Subtitle
title12 = tk.Label(rules12, text = "                              HOW TO PLAY?                             ", font = fontStyle6, bg = "#fdd501")
title12.pack()
subtitle12 = tk.Label(rules12, text = "                                Emoji to Expression!                               ", font = fontStyle7, bg = "#fdd501")
subtitle12.pack()

#BG Image
rule12img = ImageTk.PhotoImage(Image.open("Media/kuning.jpg"))
rule12bg = tk.Label(rules12, image = rule12img)
rule12bg.pack()

#Rule
rule12 = tk.Label(rules12, text = "2. You need to express the same expression as the given emoji.", bg = "#fdd501")
rule12.place(x = 180, y = 180)

#Button
butRule12l = tk.Button(rules12, cursor = "hand2", text = "<<<", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules11))
butRule12l.place(x = 40, y = 270)
butRule12r = tk.Button(rules12, cursor = "hand2", text = ">>>", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules13))
butRule12r.place(x = 630, y = 270)


#Game 1 - Rule 3

#Title and Subtitle
title13 = tk.Label(rules13, text = "                               HOW TO PLAY?                             ",font = fontStyle6, bg = "#fdd501")
title13.pack()
subtitle13 = tk.Label(rules13, text = "                                Emoji to Expression!                               ",font = fontStyle7, bg = "#fdd501")
subtitle13.pack()

#BG Image
rule13img = ImageTk.PhotoImage(Image.open("Media/kuning.jpg"))
rule13bg = tk.Label(rules13, image = rule13img)
rule13bg.pack()

#Rule
rule13 = tk.Label(rules13, text = "3. If you success, you will get a point.", bg = "#fdd501")
rule13.place(x = 250, y = 180)

#Button
butRule13l = tk.Button(rules13, cursor = "hand2", text = "<<<", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules12))
butRule13l.place(x = 40, y = 270)
butRule13r = tk.Button(rules13, cursor = "hand2", text = ">>>", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules14))
butRule13r.place(x = 630, y = 270)

#Game 1 - Rule 4

#Title and Subtitle
title14 = tk.Label(rules14, text = "                              HOW TO PLAY?                             ",
                   font = fontStyle6, bg = "#fdd501")
title14.pack()
subtitle14 = tk.Label(rules14, text = "                                Emoji to Expression!                               ",
                      font = fontStyle7, bg = "#fdd501")
subtitle14.pack()

#BG Image
rule14img = ImageTk.PhotoImage(Image.open("Media/kuning.jpg"))
rule14bg = tk.Label(rules14, image = rule14img)
rule14bg.pack()

#Rule
rule14 = tk.Label(rules14, text = "4. If you failed, you have another chance to guess the emoji again.", bg = "#fdd501")
rule14.place(x = 170, y = 180)

#Button
butRule14l = tk.Button(rules14, cursor = "hand2", text = "<<<", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules13))
butRule14l.place(x = 40, y = 270)
butRule14r = tk.Button(rules14, cursor = "hand2", text = ">>>", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules15))
butRule14r.place(x = 630, y = 270)

#Game 1 - Rule 5

#Title and Subtitle
title15 = tk.Label(rules15, text = "                              HOW TO PLAY?                             ",
                   font = fontStyle6, bg = "#fdd501")
title15.pack()
subtitle15 = tk.Label(rules15, text = "                                Emoji to Expression!                               ",
                      font = fontStyle7, bg = "#fdd501")
subtitle15.pack()

#BG Image
rule15img = ImageTk.PhotoImage(Image.open("Media/kuning.jpg"))
rule15bg = tk.Label(rules15, image = rule15img)
rule15bg.pack()

#Rule
rule15 = tk.Label(rules15, text = "5. If you have failed for 3 times, the game will generate another emoji for you.",
                  bg = "#fdd501")
rule15.place(x = 150, y = 180)

#Button
butRule15l = tk.Button(rules15, cursor = "hand2", text = "<<<", height = 15, bg = "black", fg = "#fdd501",
                       command = lambda: raise_frame(rules14))
butRule15l.place(x = 40, y = 270)
butBackHTP1 = tk.Button(rules15, cursor = "hand2", text="Back to Rules", bg = "black", fg = "#fdd501",
                        command=lambda: raise_frame(htp))
butBackHTP1.place(x = 300, y = 600)

#----------------------

#2NDGAMERULES

#Game 2 - Rule 1

#Title and Subtitle
title21 = tk.Label(rules21, text = "                              HOW TO PLAY?                             ",
                   font = fontStyle6, bg = "black", fg = "#fdd501")
title21.pack()
subtitle21 = tk.Label(rules21, text = "                                Expression to Emoji!                               ",
                      font = fontStyle7, bg = "black", fg = "#fdd501")
subtitle21.pack()

#BG Image
rule21img = ImageTk.PhotoImage(Image.open("Media/hitam.jpg"))
rule21bg = tk.Label(rules21, image = rule21img)
rule21bg.pack()

#Rule
rule21 = tk.Label(rules21, text = "1. The game will ask for your expression.", bg = "black", fg = "#fdd501")
rule21.place(x = 235, y = 180)

#Button
butRule21r = tk.Button(rules21, cursor = "hand2", text = ">>>", height = 15, bg = "#fdd501",
                       command = lambda: raise_frame(rules22))
butRule21r.place(x = 630, y = 270)

#Game 2 - Rule 2

#Title and Subtitle
title22 = tk.Label(rules22, text = "                              HOW TO PLAY?                             ",
                   font = fontStyle6, bg = "black", fg = "#fdd501")
title22.pack()
subtitle22 = tk.Label(rules22, text = "                                Expression to Emoji!                               ",
                      font = fontStyle7, bg = "black", fg = "#fdd501")
subtitle22.pack()

#BG Image
rule22img = ImageTk.PhotoImage(Image.open("Media/hitam.jpg"))
rule22bg = tk.Label(rules22, image = rule22img)
rule22bg.pack()

#Rule
rule22 = tk.Label(rules22, text = "2. The game will show an emoji that suits your expression the most.", bg = "black",
                  fg = "#fdd501")
rule22.place(x = 170, y = 180)

#Button
butRule22l = tk.Button(rules22, cursor = "hand2", text = "<<<", height = 15, bg = "#fdd501",
                       command = lambda: raise_frame(rules21))
butRule22l.place(x = 40, y = 270)
butRule22r = tk.Button(rules22, cursor = "hand2", text = ">>>", height = 15, bg = "#fdd501",
                       command = lambda: raise_frame(rules23))
butRule22r.place(x = 630, y = 270)

#Game 2 - Rule 3

#Title and Subtitle
title23 = tk.Label(rules23, text = "                              HOW TO PLAY?                             ",
                   font = fontStyle6, bg = "black", fg = "#fdd501")
title23.pack()
subtitle23 = tk.Label(rules23, text = "                                Expression to Emoji!                               ",
                      font = fontStyle7, bg = "black", fg = "#fdd501")
subtitle23.pack()

#BG Image
rule23img = ImageTk.PhotoImage(Image.open("Media/hitam.jpg"))
rule23bg = tk.Label(rules23, image = rule23img)
rule23bg.pack()

#Rule
rule23 = tk.Label(rules23, text = "3. If the emoji suits your expression, choose yes.", bg = "black", fg = "#fdd501")
rule23.place(x = 220, y = 180)

#Button
butRule22l = tk.Button(rules23, cursor = "hand2", text = "<<<", height = 15, bg = "#fdd501",
                       command = lambda: raise_frame(rules22))
butRule22l.place(x = 40, y = 270)
butRule23r = tk.Button(rules23, cursor = "hand2", text = ">>>", height = 15, bg = "#fdd501",
                       command = lambda: raise_frame(rules24))
butRule23r.place(x = 630, y = 270)

#Game 2 - Rule 4

#Title and Subtitle
title24 = tk.Label(rules24, text = "                              HOW TO PLAY?                             ",
                   font = fontStyle6, bg = "black", fg = "#fdd501")
title24.pack()
subtitle24 = tk.Label(rules24, text = "                                Expression to Emoji!                               ",
                      font = fontStyle7, bg = "black", fg = "#fdd501")
subtitle24.pack()

#BG Image
rule24img = ImageTk.PhotoImage(Image.open("Media/hitam.jpg"))
rule24bg = tk.Label(rules24, image = rule24img)
rule24bg.pack()

#Rule
rule24 = tk.Label(rules24, text = "4. If the emoji doesn't suit your expression, choose no.", bg = "black",
                  fg = "#fdd501")
rule24.place(x = 200, y = 180)

#Button
butRule24l = tk.Button(rules24, cursor = "hand2", text = "<<<", height = 15, bg = "#fdd501",
                       command = lambda: raise_frame(rules23))
butRule24l.place(x = 40, y = 270)
butBackHTP2 = tk.Button(rules24, cursor = "hand2", text="Back to Rules", bg = "#fdd501",
                        command = lambda: raise_frame(htp))
butBackHTP2.place(x = 300, y = 600)

# ----------------------

EmotionList = {1 : "angry", 2 : "happy", 3 : "sad",
               4 : "surprise", 5 : "neutral" }

def emotion_prediction(path) :
    read_img = cv2.imread(path)
    result = DeepFace.analyze(read_img, actions= ['emotion'])

    if result['dominant_emotion'] == 'disgust' or result['dominant_emotion'] == 'fear' :
        #ambil tertinggi kedua
        max_val = -1
        dominant_emotion = '-'
        for x in result['emotion'].keys() :
            if x == 'disgust' or x == 'fear' :
                continue
            val = result['emotion'][x]
            if (val > max_val):
                max_val = val
                dominant_emotion = x
        return dominant_emotion
    return result['dominant_emotion']


def detect_faces(frame) :
    face_cascade = cv2.CascadeClassifier("haarcascade.xml")

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        frame_gray,
        scaleFactor = 1.07,
        minNeighbors = 5
    )
    #global cnt
    if faces is () :
        return False
    #    print(f"No faces is found! {cnt}")
    #    cnt += 1
    #    return

    for x, y, w, h in faces:
        img = cv2.rectangle(
            frame,  # image object
            (x, y),  # posisi kotak
            (x + w, y + h),  # posisi kotak
            (0, 255, 0),  # warna kotak RGB
            3  # lebar garis kotak
        )
    return True

def run(state, lives, emoImg, emoName):
    cap = cv2.VideoCapture(0)
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    startCapture = False
    nSecond = 0
    timeElapse = 0.0
    startTime = 0.0
    strSec = '321'

    if(state == 1) :
        foreground = cv2.resize(emoImg, (100,100))
        alpha = 0.1

    while (True) :
        ret, img = cap.read()

        font = cv2.FONT_HERSHEY_COMPLEX

        #cv2.putText(img, "Text",(x,y), font, 0.7, color, bold, cv2.LINE_AA)
        cv2.putText(img, "Press SPACE: Capture", (5, 470), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, "Press Q: To Quit", (420, 470), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

        if(state == 1) :
            added_image = cv2.addWeighted(img[10:110, 10:110, :], alpha, foreground[0:100, 0:100, :], 1 - alpha, 0)

            img[10:110, 10:110] = added_image
            cv2.putText(img, emoName, (25, 120), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(img, "Lives : " + str(lives), (500,25), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

        face = detect_faces(img)

        if startCapture:
            if nSecond < 3:
                # draw nth second
                cv2.putText(img=img, text=strSec[nSecond],
                            org=(int(frameWidth / 2 - 20), int(frameHeight / 2)),
                            fontFace=cv2.FONT_HERSHEY_DUPLEX,
                            fontScale=6,
                            color=(255, 255, 255),
                            thickness=5,
                            lineType=cv2.LINE_AA)
                timeElapse = (datetime.now() - startTime).total_seconds()

                if timeElapse >= 1:
                    nSecond += 1
                    timeElapse = 0
                    startTime = datetime.now()

            else:
                img_name = "tes.png"
                cv2.imwrite(img_name, img)

                startCapture = False
                nSecond = 0
                break

        key = cv2.waitKey(1)
        if key == ord(' ') : #press space to capture
            if face == False:
                print("No faces detected, please Try again!")
            else:
                startCapture = True
                startTime = datetime.now()


        if(key == ord('q')) : #press q to quit
            break

        cv2.imshow('Capturing', img)

    cap.release()
    cv2.destroyAllWindows()


def randomPathEmoji(emotion):
    randEmo = random.randint(1,3)
    if (emotion == EmotionList[1]):  # angry
        path = 'emoji/angry/' + str(randEmo) + '.png'
    if (emotion == EmotionList[2]):  # happy
        path = 'emoji/happy/' + str(randEmo) + '.png'
    if (emotion == EmotionList[3]):  # sad
        path = 'emoji/sad/' + str(randEmo) + '.png'
    if (emotion == EmotionList[4]):  # surprise
        path = 'emoji/surprise/' + str(randEmo) + '.png'
    if (emotion == EmotionList[5]):  # neutral
        path = 'emoji/neutral/' + str(randEmo) + '.png'
    return path


def show_result_game(state,win,emoName):
    global  resultFrame
    resultFrame = Frame(window)
    resultFrame.place(x=0, y=0, width=700, height=640)

    # background
    BGimg = ImageTk.PhotoImage(Image.open("Media/Result/resultBG2.png"))
    BG = tk.Label(resultFrame, image=BGimg)
    BG.image = BGimg
    BG.pack()

    if(state == 1):
        if(win == True) :
            winEmoji = ImageTk.PhotoImage(Image.open("Media/Result/win2.png"))
            winText = tk.Label(resultFrame, text="Congrast !!! You WIN the game", font=fontStyle18, bg="#dab126")
            winText.place(x=130, y=380)
        else :
            winEmoji = ImageTk.PhotoImage(Image.open("Media/Result/lose2.png"))
            winText = tk.Label(resultFrame, text="You Failed ! Try Again and Keep Fighting", font=fontStyle18, bg="#dab126")
            winText.place(x=60, y=380)
        win = tk.Label(resultFrame,image=winEmoji, bg="#dab126")
        win.image = winEmoji
        win.place(x=250, y=200)
    else :
        ##Imitate emoji
        image = Image.open(randomPathEmoji(emoName))
        image = image.resize((200, 200), Image.ANTIALIAS)
        winEmoji = ImageTk.PhotoImage(image)
        win = tk.Label(resultFrame, image=winEmoji, bg="#dab126")
        win.image = winEmoji
        win.place(x=250, y=200)
        # text
        winText = tk.Label(resultFrame,text="Congrast !!! You Got This Emoji", font=fontStyle18, bg="#dab126")
        winText.place(x=130, y=380)

    MainMenuBut = tk.Button(resultFrame,text="Main Menu", font=fontStyle19, bg="#dab126", command = lambda: raise_frame(menu))
    MainMenuBut.place(x=200, y=440)

    if(state == 1) :
        PlayAgainBut = tk.Button(resultFrame,text="Play Again", font=fontStyle19, bg="#dab126", command = lambda : game1_start())
    else :
        PlayAgainBut = tk.Button(resultFrame, text="Play Again", font=fontStyle19, bg="#dab126",
                                 command=lambda: game2_start())
    PlayAgainBut.place(x=320, y=440)

    ExitBut = tk.Button(resultFrame, text="     Exit     ", font=fontStyle19, bg="#dab126", command = close_window)
    ExitBut.place(x=430, y=440)

    raise_frame(resultFrame)


# OPENCAMERAGAME1

def game1_start() :

    # lives
    lives = 3
    win = False

    emoName = EmotionList[random.randint(1, 5)]
    emoImg = cv2.imread(randomPathEmoji(emoName))
    emoImg = cv2.resize(emoImg, (100,100))

    while (lives > 0):
        # open cam
        run(1,lives,emoImg,emoName)

        # analyse expression
        imgPlayer = 'tes.png'
        emotion = emotion_prediction(imgPlayer)
        print(emotion)

        # show result -> same or not
        if (emotion == emoName):
            print('Congratulation!')
            win = True
            break
        else:
            lives -= 1

    if (lives <= 0):
        print('You failed')
        win = False

    show_result_game(1,win,"")

# ----------------------

# OPENCAMERAGAME2

def game2_start():

    #open camera
    run(2,0,"","");

    #analyze emoji
    img_name = 'tes.png'
    emotion = emotion_prediction(img_name)
    print(emotion)
    #print('Your emotion : ' + format(emotion['emotion'][emotion['dominant_emotion']], '.2f')
    #      + '% ' + emotion['dominant_emotion'])
    print('Your emotion : ' + emotion)

    show_result_game(2,0,emotion)

window.mainloop()