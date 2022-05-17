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
import itertools
import os.path
import threading
from PIL import Image
#Загрузка
if os.path.exists('save0.filec'):
    with open('save0.filec',"r") as f:
        data = dict(json.load(f))
    money = data['money']
    health = data['health']
    lv = data['lv']
    exp = data['exp']
    inv = data['inv']
    arm = data['arm']
    name = data['name']
else:
    money= 0
    health = 100
    lv = 1
    exp = 0
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
    arm = {
    'armorOne' : 0,
    'armorTwo' : 0,
    'armorThree' : 0,
    'armorFour' : 0
    }
    name = "Player"
    savedata = {
    'money' : money,
    'health' : health,
    'lv' : lv,
    'exp' : exp,
    'inv' : inv,
    'arm' : arm,
    'name' : name
    }
    with open('save0.filec',"w") as f:
        json.dump(savedata,f)
# Функции загрузки/сохранения
def save():
    global money
    global health
    global lv
    global exp
    global inv
    global arm
    global name
    savedata = {
    'money' : money,
    'health' : health,
    'lv' : lv,
    'exp' : exp,
    'inv' : inv,
    'arm' : arm,
    'name' : name
    }
    with open('save0.filec',"w") as f:
        json.dump(savedata,f)
def load():
    with open('save0.filec',"r") as f:
        data = dict(json.load(f))
    money = data['money']
    health = data['health']
    lv = data['lv']
    exp = data['exp']
    inv = data['inv']
    arm = data['arm']
    name = data['name']
# Обьект блока
class Block():
    def __init__(self,x,y,id,canvas,root):
        self.x = x
        self.y = y
        self.id = id
        self.canvas = canvas
        self.root = root
        self.image = ImageTk.PhotoImage(Image.open(f'{id}.png'))
    def getId(self):
        return self.id
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def visualise(self):
        self.windowv = Label(self.root,self.canvas,image = self.image)
        self.windowv.pack()
        self.window = self.canvas.create_window(self.x,self.y,window = self.windowv)
#Загрузка, создание, и визуализация блоков
blocks = []
def visualise():
    pass
# Функция обновления
def Update(canvas,root):
    pass
root = Tk()
root.title("ComiRun")
visualise()
#threading.start_new_thread(update,(canvas,root))
root.mainloop()
