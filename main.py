"""
Главный файл
"""
import math
import time
from tkinter import *
import json
import os
import time
import shutil
import itertools
import os.path
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
    money = 0
    health = 100
    lv = 1
    exp = 0
    inv = {
    slot1 = 0,
    slot2 = 0,
    slot3 = 0,
    slot4 = 0,
    slot5 = 0,
    slot6 = 0,
    slot7 = 0,
    slot8 = 0,
    }
    slot9 = 0
    arm = {
    armorOne = 0,
    armorTwo = 0,
    armorThree = 0,
    armorFour = 0
    }
    name = "Player"
    savedata = {
    money = money,
    health = health,
    lv = lv,
    exp = exp,
    inv = inv,
    arm = arm,
    name = name
    }
    with open('save0.filec',"w") as f:
        json.dump(savedata,f)
