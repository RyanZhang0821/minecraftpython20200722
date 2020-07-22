# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:37:04 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time

pos=mc.player.getPos()

while True:
    x=pos.x+random.uniform(-10,-100)
    y=pos.y+30
    z=pos.z+random.uniform(-10,10)
    
    mc.spawnEntity(x,y,z,50)
    time.sleep(0.000001)