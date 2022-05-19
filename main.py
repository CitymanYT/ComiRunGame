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
    name = "Player"
    savedata = {
    'money' : money,
    'weapon': weapon,
    'lv' : lv,
    'exp' : exp,
    'inv' : inv,
    'armsets' : armsets,
    'curretarmor' : curretarmor,
    'name' : name,
    'progress_unlocked' : progress_unlocked
    }
    with open('save0.filec',"w") as f:
        json.dump(savedata,f)
#Режим разработчика
if dev == 1:
    money = -1
    lv = 10000
    exp = 0
    progress_unlocked = 10
    name = "Dev"
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
    global name
    global data
    savedata = {
    'money' : money,
    'weapon': weapon,
    'lv' : lv,
    'exp' : exp,
    'inv' : inv,
    'armsets' : armsets,
    'curretarmor' : curretarmor,
    'name' : name,
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
    for i in blocks():
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
user = User(0,200)
#Мобы
mobs = []
class Mob():
    def __init__(self,typ,canvas):
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
def start_battle(root,canvas):
    visualise()
    root.title("ComiRun - battle")
    user.visualise()
    for i in mobs:
        for d in i:
            d.visualise()
            d.spawn(random.randint(200,2000),random.randint(200,1000))
    root.after(100,Update(root,canvas))
def end_battle(winstate):
    if winstate == "win":
        global exp
        exp = exp + 1
    else:
        pass
#Обьекты
curretmusic = "file.ogg"
musicduration = 0
version = "1.0"
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
root = Tk()
if dev == 0:
    root.title("ComiRun")
else:
    root.title("ComiRun - Dev version.")
root.after(musicduration,MusicControl(curretmusic))
canvas = Canvas(root)
canvas.pack()
game_start = Button(canvas,function=start_battle(root,canvas),text="Начать бой.")
game_start.pack()
root.mainloop()
