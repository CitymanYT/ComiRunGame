"""
Главный файл
"""
#Модули
import math
import time
from tkinter import *
import json
import os
import time
import shutil
import random
import itertools
import os.path
import threading
from PIL import Image
#Режим разработчика
dev = 0
if os.path.exists('devfile.filec'):
    dev = 1
else:
    dev = 0
#Уровни
levelapp = {
    'one': 10,
    'two': 20
}
#levelformule = levelapp + levelapp
#Индикатор запуска
running = False
#Типы генерации
maps = {
    'default' : {10 : 'grass',9 : 'stone',4:'endlevel'}
}
#Типы брони
armors = {
    0: "empty",
    1: "stone",
    2: "gold",
    3: "iron",
    4: "diamond"
}
#Полный экран
fullscreen = 0
#Загрузка
if os.path.exists('save0.filec'):
    with open('save0.filec',"r") as f:
        data = dict(json.load(f))
    money = data['money']
    lv = data['lv']
    exp = data['exp']
    weapon = data['weapon']
    inv = data['inv']
    curretarmor = data['curretarmor']
    armsets = data['armsets']
    progress_unlocked = data['progress_unlocked']
else:
    money= 0
    lv = 1
    progress_unlocked = 0
    exp = 0
    if dev == 1:
        money = -1
        lv = 1000000
        exp = 0
        progress_unlocked = 10
    weapon = 0
    inv = {
    "slot1" : 0,
    "slot2" : 0,
    "slot3" : 0,
    "slot4" : 0,
    "slot5" : 0,
    "slot6" : 0,
    "slot7" : 0,
    "slot8" : 0,
    "slot9" : 0
    }
    curretarmor = 0
    armsets = {
    'armorOne' : 0,
    'armorTwo' : 0,
    'armorThree' : 0,
    'armorFour' : 0
    }
    savedata = {
    'money' : money,
    'weapon': weapon,
    'lv' : lv,
    'exp' : exp,
    'inv' : inv,
    'armsets' : armsets,
    'curretarmor' : curretarmor,
    'progress_unlocked' : progress_unlocked
    }
    with open('save0.filec',"w") as f:
        json.dump(savedata,f)
#Авторы
authors = ["CitymanYT","Artem Shu","Nikita S."]
#Режим разработчика
if dev == 1:
    money = -1
    lv = 10000
    exp = 0
    progress_unlocked = 10
# Функции загрузки/сохранения
def save():
    global money
    global weapon
    global lv
    global exp
    global inv
    global armsets
    global curretarmor
    global progress_unlocked
    global data
    savedata = {
    'money' : money,
    'weapon': weapon,
    'lv' : lv,
    'exp' : exp,
    'inv' : inv,
    'armsets' : armsets,
    'curretarmor' : curretarmor,
    'progress_unlocked' : progress_unlocked
    }
    with open('save0.filec',"w") as f:
        json.dump(savedata,f)
def load():
    global money
    global lv
    global exp
    global weapon
    global inv
    global curretarmor
    global armsets
    global progress_unlocked
    global data
    with open('save0.filec',"r") as f:
        data = dict(json.load(f))
    money = data['money']
    lv = data['lv']
    exp = data['exp']
    weapon = data['weapon']
    inv = data['inv']
    curretarmor = data['curretarmor']
    armsets = data['armsets']
    progress_unlocked = data['progress_unlocked']
# Обьект блока
class Block():
    def __init__(self,x,y,id,canvas,root):
        self.x = x
        self.y = y
        self.id = id
        self.canvas = canvas
        self.root = root
        self.image = PhotoImage(Image.open(f'{id}.png'))
    def getId(self):
        return self.id
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def visualise(self):
        self.windowv = Label(self.canvas,image = self.image)
        self.windowv.pack()
        self.window = self.canvas.create_window(self.x,self.y,window = self.windowv)
#Загрузка, создание, и визуализация блоков
blocks = []
def visualise():
    #Визуализация блоков
    for i in blocks:
        for d in i:
            d.visualise()
#Обьект персонажа и его визуализация
class User(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = PhotoImage(Image.open('user.png'))
        self.pastx = self.x
        self.pasty = self.y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def visualise(self):
        self.windowv = Label(self.canvas,image = self.image)
        self.windowv.pack()
        self.window = self.canvas.create_window(self.x,self.y,window = self.windowv)
    def Update(self):
        if self.x != self.pastx:
            while self.x  != self.pastx:
                if self.x < self.pastx:
                    self.pastx = self.pastx - 20
                    self.canvas.move(-20,0,self.window)
                else:
                    self.pastx = self.pastx + 20
                    self.canvas.move(20,0,self.window)
        if self.y != self.pasty:
            while self.y  != self.pasty:
                if self.y < self.pasty:
                    self.pasty = self.pasty - 20
                    self.canvas.move(0,-20,self.window)
                else:
                    self.pasty = self.pasty + 20
                    self.canvas.move(0,20,self.window)
#user = User(0,200)
#Мобы
mobs = []
class Mob():
    def __init__(self,type,canvas):
        self.type = type
        self = self
        self.canvas = canvas
        self.image = f"{type}.png"
    def visualise(self,x,y):
        self.windowv = Label(self.canvas,image = self.image)
        self.windowv.pack()
        self.window = self.canvas.create_window(self.x,self.y,window = self.windowv)
    def Update(self):
        if self.x != self.pastx:
            while self.x  != self.pastx:
                if self.x < self.pastx:
                    self.pastx = self.pastx - 20
                    self.canvas.move(-20,0,self.window)
                else:
                    self.pastx = self.pastx + 20
                    self.canvas.move(20,0,self.window)
        if self.y != self.pasty:
            while self.y  != self.pasty:
                if self.y < self.pasty:
                    self.pasty = self.pasty - 20
                    self.canvas.move(0,-20,self.window)
                else:
                    self.pasty = self.pasty + 20
                    self.canvas.move(0,20,self.window)
    def spawn(self,x,y):
        self.spawned = True
        self.alive = True
        self.x = x
        self.y = y
        self.spawnedloop()
    def spawnedloop(self):
        while self.alive:
            if self.spawned():
                self.visualise(self.x,self.y)
            if self.hp <= 0:
                self.alive = False 
#Битвы
def start_battle():
    global root
    global canvas
    global game_start
    global musicbutt
    global al
    global winstate
    global sv
    global lo
    global lvvar
    global expvar
    global lvt
    global expv
    global expt
    global lvv
    global expn
    lvt.destroy()
    expv.destroy()
    expt.destroy()
    lvv.destroy()
    expn.destroy()
    sv.destroy()
    lo.destroy()
    winstate = "quit"
    musicbutt.destroy()
    game_start.destroy()
    al.destroy()
    global endbat
    global health
    global mobcount
    global mobs
    mobcount = lv * 5
    health = 100
    endbat = Button(canvas,text="Выйти из битвы.",command=end_battle)
    endbat.pack()
    #visualise()
    root.title("ComiRun - battle")
    #user.visualise()
    #for i in mobs:
        #for d in i:
            #d.visualise()
            #d.spawn(random.randint(200,1000),200)
            #if d.health <= 0:
            #   mobcount = mobcount - 1    
    if health <= 0:
        winstate = "died"
        end_battle()
    if mobcount <= 0:
        winstate = "win"
        end_battle()
    #root.after(100,Update(root,canvas))
def end_battle():
    global canvas
    global root
    global winstate
    global endbat
    endbat.destroy()
    if winstate == "win":
        global exp
        global lv
        exp = exp + 5
        while exp >= lv * 10:
            exp = exp - lv * 10
            lv = lv + 1
        mainmenu(root,canvas)
    elif winstate == "quit":
        mainmenu(root,canvas)
    else:
        mainmenu(root,canvas)
#Обьекты
musicduration = 0
version = "1.0.1"
# Функция обновления
def Update(root,canvas):
    global user
    user.Update()
    global blocks
    for i in blocks:
        for d in i:
            d.Update()
    for i in blocks:
        for d in i:
            if d.getX() == user.getX():
                user.x = user.x + 10
                user.Update()
                if d.getX() == user.getX():
                    user.x = user.x - 20
                Update()
    root.after(100,Update(root,canvas))
def MusicControl(curretmusic):
    #Music.play(curretmusic)
    global musicduration
    global root
    root.after(musicduration,MusicControl(curretmusic))
#Потоки(музыка)
import pygame
pygame.mixer.init()
stopEntity = False
stopMusic = False
music = "musictest.mp3"
musicduration = 0
class Music(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(100)
    def run(self):
        print("""Внимание! Невозможно загрузить музыку в том же потоке.
        Выполняю загрузку другого потока....
        Успешно!""")
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(100)
    def runMusic(self):
        pygame.mixer.music.play(loops=-1)
    def stopMusic(self):
        pygame.mixer.music.stop()
def call_mus():
    global musicbutt
    global stopMusic
    global musicthread
    if stopMusic == False:
        musicbutt['text'] = "Включить музыку. Текущее состояние - выкл."
        musicthread.stopMusic()
        stopMusic = True
    else:
        musicbutt['text'] = "Включить музыку. Текущее состояние - вкл."
        musicthread.runMusic()
        stopMusic = False
def mainmenu(root,canvas):
    global game_start
    global musicbutt
    global al
    global dev
    global sv
    global lo
    global lv
    global exp
    if dev == 0:
        root.title("ComiRun")
    else:
        root.title("ComiRun - Dev version.")
    game_start = Button(canvas,command=start_battle,text="Начать бой.")
    game_start.pack()
    musicbutt = Button(canvas,command=call_mus,text = "Включить музыку. Текущее состояние - вкл.")
    musicbutt.pack()
    al = Label(canvas,text=f"CoriRun 2022 - 2022. Авторы: {str(authors)}")
    al.pack()
    sv = Button(canvas,command=save,text = "Сохранится")
    sv.pack()
    lo = Button(canvas,command=load,text= "Загрузиться")
    lo.pack()
    global lvvar
    global expvar
    global lvt
    global expv
    global expt
    global lvv
    global expn
    lvt =  Label(canvas,text="Уровень:")
    lvt.pack()
    lvv = Label(canvas,textvariable=lvvar)
    lvv.pack()
    expt = Label(canvas,text="Текущие очки:")
    expt.pack()
    expv = Label(canvas,textvariable=expvar)
    expv.pack()
    expn = Label(canvas,text=f"Осталось до повышения: {exp}/{lv*10}")
    expn.pack()
#Окно
root = Tk()
if fullscreen == 1:
    root.state('zoomed')
else:
    root.geometry("1000x500")
if dev == 0:
    root.title("ComiRun")
else:
    root.title("ComiRun - Dev version.")
#root.after(musicduration,MusicControl(curretmusic))
canvas = Canvas(root,bg="green")
canvas.pack(expand=1,fill="both")
musicthread = Music(1,"MusicThread")
musicthread.start()
lvvar = IntVar()
lvvar.set(lv)
expvar = IntVar()
expvar.set(exp)
stopMusic = True
stopEntity = True
running = True
mainmenu(root,canvas)
call_mus()
root.mainloop()
musicthread.stopMusic()