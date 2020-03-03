#!/usr/bin/python
#Import Minecraft
import mcpi.minecraft
#Import math (for sphere function)
import math
#Detect key presses. If you don't have this, do: pip3 install pynput
from pynput.keyboard import Key, Listener

#Less typing for me :)
mc = mcpi.minecraft.Minecraft.create()
#some global variables that I need
worldType = 0
#Will equal 1, void, 2, small superflat, 3, large superflat.
blockID = 0
#Most functions need to know which block you want.
func = 1
#What function is currently toggled. See change_function() for more information.
delete = 0
#How many more presses until world is toggled.

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

def cuboid(data, ID, x1, x2, y1, y2, z1, z2):
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
    mc.setBlocks(x1, y1 - 1 , z1, x2, y2 - 1, z2, ID, data)
    if pos1x != pos2x and pos1y != pos2y and pos1z != pos2z:
        mc.setBlocks(x1 + 1, y1, z1 + 1, x2 - 1, y2 - 2, z2 - 1, 0)

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
    mc.setBlocks(x1, y1 - 1 , z1, x2, y2 - 1, z2, ID, data)
    if pos1x != pos2x and pos1y != pos2y and pos1z != pos2z:
        mc.setBlocks(x1 + 1, y1 - 1, z1 + 1, x2 - 1, y2 - 1, z2 - 1, 0)
    
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

#Change the function with Right Shift
def change_function():
    global func
    funcDict = {
        1 : "Cube",
        2 : "Hollow Cube",
        3 : "Sphere",
        4 : "Hollow Sphere",
        5 : "Wall"
        }
    func += 1
    if func == 6:
        func = 1
    print(funcDict[func])
    mc.postToChat(funcDict[func])

#The query you receive in your shell. I'm thinking about making it entirely in-game,
#but you wouldn't be able to see what you're typing
def setblock_query():
    global blockID, data, func
    #If cube or hollow cube
    if func == 1 or func == 2 or func == 5:
        try:
            blockID = int(input("Choose block ID: "))
        except ValueError:
            print("Invalid ID")
            return
        try:
            data = int(input("Block Data: "))
        except ValueError:
            data = 0
        if func == 1:
            cuboid(data, blockID, pos1x, pos2x, pos1y, pos2y, pos1z, pos2z)
        elif func == 2:
            hcube(data, blockID, pos1x, pos2x, pos1y, pos2y, pos1z, pos2z)
        else:
            walls(data, blockID, pos1x, pos2x, pos1y, pos2y, pos1z, pos2z)
    #If sphere or hollow sphere
    if func == 3 or func == 4:
        #Sphere position x, y and z
        sposx, sposy, sposz = mc.player.getPos()
        sposx, sposy, sposz = round(sposx), round(sposy), round(sposz)
        #The centerpoint values that will be inputted into the sphere function 
        print(sposx, " ", sposy, " ", sposz)
        try:
            blockID = int(input("Choose block ID: "))
        except ValueError:
            return
        try:
            data = int(input("Block Data: "))
        except ValueError:
            data = 0
        try:
            radius = int(input("Radius: "))
        except ValueError:
            return
        if func == 3:
            sphere(radius, sposx, sposy, sposz, blockID, data)
        if func == 4:
            hsphere(radius, sposx, sposy, sposz, blockID, data)

#This somehow detects key presses, I don't know how.
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
        

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()