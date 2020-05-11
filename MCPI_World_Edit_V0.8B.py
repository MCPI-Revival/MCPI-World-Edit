#!/usr/bin/python
#Welcome to the mess that is my code!
#I'm mostly self-taught, so I'm sorry in advance if I don't follow conventions perfectly.

#Import Minecraft
import mcpi.minecraft
#Import math (for sphere function)
import math
#Import random (for replace & replacenear functions)
import random
#Detect key presses. If you don't have this, do: pip3 install pynput
from pynput.keyboard import Key, Listener

#Less typing for me :)
mc = mcpi.minecraft.Minecraft.create()
#some global variables that I need
worldType = 0
#Will equal 1, void, 2, small superflat, 3, large superflat.
ID = 0
#Most functions need to know which block you want.
func = 1
#What function is currently toggled. See change_function() for more information.
delete = 0
#How many more presses until world is toggled.

#Partial credit to:
#https://arghbox.wordpress.com/2013/08/18/minecraft-pi-api-getting-blocks/
def replace(oldIDList, newIDList, oldDataList, newDataList, x1, y1, z1, x2, y2, z2):
    #Don't you just love that feeling when you have 10 parameters to pass in?
    xhigh = max(x1, x2)
    xlow = min(x1, x2)
    yhigh = max(y1, y2)
    ylow = min(y1, y2)
    zhigh = max(z1, z2)
    zlow = min(z1, z2)
    blocksChangedCount = 0
    for x in range(xhigh - xlow + 1):
        for y in range(yhigh - ylow + 1):
            for z in range(zhigh - zlow + 1):
                block = mc.getBlockWithData(xlow + x, ylow + y, zlow + z)
                coords = (xlow + x, ylow + y, zlow + z)
                print("Block at: " + str(coords))
                print("ID: " + str(block.id) + " Data: " + str(block.data))
                if block.id in oldIDList:
                    if oldDataList[oldIDList.index(block.id)] == block.data:
                        blocksChangedCount += 1
                        lengthNewIDList = len(newIDList)
                        if lengthNewIDList > 1: 
                            newID = newIDList[random.randint(0, len(newIDList) - 1)]
                            mc.setBlock(xlow + x, ylow + y, zlow + z, newID, newDataList[newIDList.index(newID)])
                        else:
                            mc.setBlock(xlow + x, ylow + y, zlow + z, newIDList[0], newDataList[0])
    mc.postToChat("Operation complete. " + str(blocksChangedCount) + " blocks were affected.")

def replacenear(oldIDList, newIDList, oldDataList, newDataList, radius, x, y, z):
    x1 = x - radius
    x2 = x + radius
    y1 = y - radius
    y2 = y + radius
    z1 = z - radius
    z2 = z + radius
    xhigh = max(x1, x2)
    xlow = min(x1, x2)
    yhigh = max(y1, y2)
    ylow = min(y1, y2)
    zhigh = max(z1, z2)
    zlow = min(z1, z2)
    blocksChangedCount = 0
    for x in range(xhigh - xlow + 1):
        for y in range(yhigh - ylow + 1):
            for z in range(zhigh - zlow + 1):
                block = mc.getBlockWithData(xlow + x, ylow + y, zlow + z)
                coords = (xlow + x, ylow + y, zlow + z)
                print("Block at: " + str(coords))
                print("ID: " + str(block.id) + " Data: " + str(block.data))
                if block.id in oldIDList:
                    if oldDataList[oldIDList.index(block.id)] == block.data:
                        blocksChangedCount += 1
                        lengthNewIDList = len(newIDList)
                        if lengthNewIDList > 1: 
                            newID = newIDList[random.randint(0, len(newIDList) - 1)]
                            mc.setBlock(xlow + x, ylow + y, zlow + z, newID, newDataList[newIDList.index(newID)])
                        else:
                            mc.setBlock(xlow + x, ylow + y, zlow + z, newIDList[0], newDataList[0])
    mc.postToChat("Operation complete. " + str(blocksChangedCount) + " blocks were affected.")

def getPos1():
    global pos1x, pos1y, pos1z
    pos1x, pos1y, pos1z = mc.player.getTilePos() #Formerly getpos(), but getTilePos() is more accurate.
    mc.postToChat("Pos 1 is set to (" + str(pos1x) + ", " + str(pos1y) + ", " + str(pos1z) + ")")

def getPos2():
    global pos2x, pos2y, pos2z
    pos2x, pos2y, pos2z = mc.player.getTilePos()
    mc.postToChat("Pos 2 is set to (" + str(pos2x) + ", " + str(pos2y) + ", " + str(pos2z) + ")")

def cuboid(data, ID, x1, x2, y1, y2, z1, z2):
    #We subtract 1 from y since getTilePos() will actually return your leg position.
    int(ID)
    mc.setBlocks(x1, y1 - 1 , z1, x2, y2 - 1, z2, ID, data)
    
def hcube(data, ID, x1, x2, y1, y2, z1, z2):
    buf = 0
    int(ID)
    if x1 > x2:
        buf = x2
        x2 = x1
        x1 = buf
    if y1 > y2:
        buf = y2
        y2 = y1
        y1 = buf
    if z1 > z2:
        buf = z2
        z2 = z1
        z1 = buf
    #This used to create a cube then a cube of air inside of it, but that deletes the insides (not good)
    mc.setBlocks(x1, y1 - 1, z2, x2, y2 - 1, z2, ID, data) #Back wall
    mc.setBlocks(x1, y1 - 1, z1, x2, y2 - 1, z1, ID, data) #Front wall
    mc.setBlocks(x1, y1 - 1, z1, x1, y2 - 1, z2, ID, data) #Left wall
    mc.setBlocks(x2, y1 - 1, z1, x2, y2 - 1, z2, ID, data) #Right wall
    mc.setBlocks(x1, y1 - 1, z1, x2, y1 - 1, z2, ID, data) #Floor
    mc.setBlocks(x1, y2 - 1, z1, x2, y2 - 1, z2, ID, data) #Roof
    
#Creates walls given 2 points and block + data
def walls(data, ID, x1, x2, y1, y2, z1, z2):
    buf = 0
    int(ID)
    if x1 > x2:
        buf = x2
        x2 = x1
        x1 = buf
    if y1 > y2:
        buf = y2
        y2 = y1
        y1 = buf
    if z1 > z2:
        buf = z2
        z2 = z1
        z1 = buf
        z1 = buf
    mc.setBlocks(x1, y1 - 1, z2, x2, y2 - 1, z2, ID, data) #Back wall
    mc.setBlocks(x1, y1 - 1, z1, x2, y2 - 1, z1, ID, data) #Front wall
    mc.setBlocks(x1, y1 - 1, z1, x1, y2 - 1, z2, ID, data) #Left wall
    mc.setBlocks(x2, y1 - 1, z1, x2, y2 - 1, z2, ID, data) #Right wall
    
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

#This is the equation that will tell the distance between two points in a sphere.
#** means "to the power of"
def spherical_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))

#Make a sphere with a given radius and centerpoint
def sphere(radius, x1, y1, z1, ID, data):
    #x1, y1, and z1 are the center coordinates
    #Teleport player upward so that they aren't trapped in the sphere
    #This MAY through up an error. Python sometimes thinks that I'm
    #calling a tuple, not a function.
    px, py, pz = mc.player.getPos()
    mc.player.setPos(px, py + radius + 1, pz)
    diameter = radius * 2
    #First item in tuple is the start point, second is end point
    xcoords = (x1 - radius, x1 + radius)
    ycoords = (y1 - radius, y1 + radius)
    zcoords = (z1 - radius, z1 + radius)
    #More or less we are checking every point in a cuboid with the given radius, and checking each block.
    #We calculate if the block is within the sphere with the Pythagorean Theorum, and if it is, set it to the
    #given block with the given data
    for x2 in range(xcoords[0], xcoords[1]):     
        for y2 in range(ycoords[0], ycoords[1]):
            for z2 in range(zcoords[0], zcoords[1]):
                if spherical_distance(x1, y1, z1, x2, y2, z2) <= radius:
                    mc.setBlock(x2, y2, z2, ID, data)

#Make a hollow sphere with a given radius and centerpoint (might add thickness in the future)
#Same thing as sphere, but we only set the block if it's greater that radius - 1 and less than the radius
#This will only set the outside blocks
def hsphere(radius, x1, y1, z1, ID, data):
    diameter = radius * 2
    xcoords = (x1 - radius, x1 + radius)
    ycoords = (y1 - radius, y1 + radius)
    zcoords = (z1 - radius, z1 + radius)
    for x2 in range(xcoords[0], xcoords[1]):     
        for y2 in range(ycoords[0], ycoords[1]):
            for z2 in range(zcoords[0], zcoords[1]):
                sd = spherical_distance(x1, y1, z1, x2, y2, z2)
                if sd > radius -1 and sd < radius:
                    mc.setBlock(x2, y2, z2, ID, data)

def center(data, ID, x1, x2, y1, y2, z1, z2):
    buf = 0
    if x1 > x2:
        buf = x2
        x2 = x1
        x1 = buf
    if z1 > z2:
        buf = z2
        z2 = z1
        z1 = buf
    if y1 > y2:
        buf = y2
        y2 = y1
        y1 = buf
    x = (x2 + x1) / 2
    z = (x2 + z1) / 2
    y = (y2 + y1) / 2
    x, y, z = round(x), round(y), round(z)
    mc.setBlock(x, y - 1, z, ID, data)

#Change the function with Right Shift
def change_function():
    global func
    funcDict = {
        1 : "Cube",
        2 : "Hollow Cube",
        3 : "Sphere",
        4 : "Hollow Sphere",
        5 : "Wall",
        6 : "Center",
        7 : "Replace",
        8 : "Replace Near"
        }
    func += 1
    if func == 9:
        func = 1
    print(funcDict[func])
    mc.postToChat(funcDict[func])

#The query you receive in your shell. I'm thinking about making it entirely in-game,
#but you wouldn't be able to see what you're typing

def setblock_query():
    global ID, data, func #Global variable this function needs
    if not func == 7 and not func == 8: #If the function isn't replace or replace near
        try:
            ID = int(input("Choose block ID: ")) #Get block ID from user
        except ValueError:
            print("Invalid ID") #If user passes in non-integer
            return
        try:
            data = int(input("Block Data: ")) #Get block data from user
        except ValueError:
            print("Invalid Data, assuming 0.") #If user passes in non-integer
            data = 0
    if func == 1: #Cube
        cuboid(data, ID, pos1x, pos2x, pos1y, pos2y, pos1z, pos2z)
    elif func == 2: #Hollow Cube
        hcube(data, ID, pos1x, pos2x, pos1y, pos2y, pos1z, pos2z)
    elif func == 3 or func == 4: #Sphere or Hollow Sphere
        sposx, sposy, sposz = mc.player.getTilePos() #Get position for Sphere center
        try:
            radius = int(input("Radius: "))
        except ValueError:
            print("Invalid Radius")
            return
        if func == 3: #Sphere
            sphere(radius, sposx, sposy, sposz, ID, data)
        if func == 4: #Hollow Sphere
            hsphere(radius, sposx, sposy, sposz, ID, data)
    if func == 5: #Walls
        walls(data, ID, pos1x, pos2x, pos1y, pos2y, pos1z, pos2z)
    if func == 6: #Center
        center(data, ID, pos1x, pos2x, pos1y, pos2y, pos1z, pos2z)
    if func == 7 or func == 8: #Replace, Replace near
        #I really wish this was simpler.
        oldIDList = []
        newIDList = []
        oldDataList = []
        newDataList = []
        try:
            oldIDListLength = int(input("How many types of blocks would you like to replace? "))
        except ValueError:
            print("Invalid number")
            return
        for i in range(oldIDListLength):
            try:
                oldID = int(input("ID of Block to be replaced " + str(i + 1) + "/" + str(oldIDListLength) + " "))
                oldIDList.append(oldID)
            except ValueError:
                print("Invalid ID")
                return
            try:
                oldData = int(input("Data of Block to be replaced " + str(i + 1) + "/" + str(oldIDListLength) + " "))
            except ValueError:
                print("Invalid Data, assuming 0.")
                oldData = 0
            oldDataList.append(oldData)
        try:
            newIDListLength = int(input("How many different blocks would you like to replace them with? "))
        except ValueError:
            print("Invalid number")
            return
        for i in range(newIDListLength):
            try:
                newID = int(input("ID of Block to be replaced " + str(i + 1) + "/" + str(newIDListLength) + " "))
                newIDList.append(newID)
            except ValueError:
                print("Invalid ID")
                return
            try:
                newData = int(input("Data of Block to be replaced " + str(i + 1) + "/" + str(newIDListLength) + " "))
            except ValueError:
                print("Invalid Data, assuming 0.")
                newData = 0
            newDataList.append(newData)
        if func == 8:
            try:
                radius = int(input("Radius to replace: "))
            except ValueError:
                print("Invalid Radius")
                return
            playerx, playery, playerz = mc.player.getTilePos()
            replacenear(oldIDList, newIDList, oldDataList, newDataList, radius, playerx, playery, playerz)
        if func == 7:
            replace(oldIDList, newIDList, oldDataList, newDataList, pos1x, pos1y, pos1z, pos2x, pos2y, pos2z)
#This somehow detects key presses, I don't know how.
#If an error gets thrown up around here, open terminal and type pip3 install pynput
def on_press(key):
    #print('{0}'.format(key))
    #uncomment above to see key presses in shell (It's super annoying)
    #Something has to be in this function, and it can't not exist, so
    #y always = 0 :P
    y = 0

#When the key is released:
def on_release(key):
    global delete
    if key == Key.up:
        #I don't want anyone to accidentally delete their world, so press the button 3 times to change
        #Note that you can hit right control to save your world
        delete += 1
        if delete == 1:
            mc.postToChat("Press 2 more times to toggle world")
        elif delete == 2:
            mc.postToChat("Press 1 more time to toggle world")
        else:
            toggle_world()
            delete = 0
    if key == Key.left:
        getPos1()
    if key == Key.right:
        getPos2()
    if key == Key.down:
        setblock_query()
    if key == Key.shift_r:
        change_function()
    if key == Key.ctrl_r:
        mc.postToChat("World saved. Press the right Alt key to load it.")
        mc.saveCheckpoint()
    if key == Key.alt_r:
        mc.postToChat("Your save has been loaded.")
        mc.restoreCheckpoint()
        

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    #Soooo close to 400 lines :P