#!/usr/bin/python
import mcpi.minecraft
import time
from pynput.keyboard import Key, Listener

mc = mcpi.minecraft.Minecraft.create()
worldType = 0
blockID = 0

def getPos1():
    global pos1x, pos1y, pos1z
    pos1x, pos1y, pos1z = mc.player.getPos()
    pos1x = round(pos1x, 0)
    pos1y = round(pos1y, 0)
    pos1z = round(pos1z, 0)
    mc.postToChat("Pos 1 is set to (" + str(pos1x) + ", " + str(pos1y) + ", " + str(pos1z) + ")")

def getPos2():
    global pos2x, pos2y, pos2z
    pos2x, pos2y, pos2z = mc.player.getPos()
    pos2x = round(pos2x, 0)
    pos2y = round(pos2y, 0)
    pos2z = round(pos2z, 0)
    mc.postToChat("Pos 2 is set to (" + str(pos2x) + ", " + str(pos2y) + ", " + str(pos2z) + ")")

def cuboid(data):
    global pos1x, pos1y, pos1z, pos2x, pos2y, pos2z, blockID
    int(blockID)
    mc.setBlocks(pos1x, pos1y - 1 ,pos1z, pos2x, pos2y - 1, pos2z, blockID, data)
    
def toggle_world():
    global worldType
    worldType += 1
    if worldType > 3:
        worldType = 1
    if worldType == 1:
        mc.postToChat("Toggled to void world")
        mc.setBlocks(-128, -64,-128, 128, 30, 128, 0)
        mc.player.setPos(0,10,0)
        mc.setBlocks(-10, 0, -10, 10, 0, 10, 1)
        mc.postToChat("Platform Created At (0, 0). Teleporting you there now.")
    if worldType == 2:
        mc.postToChat("Toggled to small superflat")
        mc.setBlocks(-128, -64, -128, 128, -64, 128, 7)
        mc.setBlocks(-128, -63, -128, 128, -62, 128, 3)
        mc.setBlocks(-128, -61, -128, 128, -61, 128, 2)
        x, y, z = mc.player.getPos()
        mc.player.setPos = x, -60, z
    if worldType == 3:
        mc.postToChat("Toggled to large superflat")
        mc.setBlocks(-128, -64, -128, 128, -64, 128, 7)
        mc.setBlocks(-128, -63, -128, 128, -50, 128, 3)
        mc.setBlocks(-128, -49, -128, 128, -49, 128, 2)
        x, y, z = mc.player.getPos()
        mc.player.setPos = x, -48, z
    return

#This somehow detects key presses, I don't know how.
def on_press(key):
    print('{0} pressed'.format(key))
    
def on_release(key):
    print('{0} pressed'.format(key))
    global blockID, data
    if key == Key.up:
        toggle_world()
    if key == Key.left:
        getPos1()
    if key == Key.right:
        getPos2()
    if key == Key.down:
        try:
            blockID = int(input("Choose block ID: "))
        except ValueError:
            return
        try:
            data = int(input("Block Data:"))
        except ValueError:
            return
        cuboid(data)

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
