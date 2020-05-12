# MCPI-World-Edit
To download the newest version, go to the releases tab
An extremely simple version of world edit for MCPI.

SETUP:
Download the code
Double-click it to open it in thonny
Make sure that minecraft is open and a world is loaded
Press the green triangle on the top of the screen to run it
Press the red square if you want to stop it

Due to the nature of MCPI multiplayer, things created by people who have connected to the world will not be seen by others.
Only things created by the host are universal.

COMMANDS:
Up arrow: Toggle between Void, Small Superflat, and Large Superflat Worlds.
The first time you do it, there will be a lot of lag.
Left arrow: Select Position 1
Right arrow: Select Position 2
Down arrow: Run command
Right control: Save game
Right alt: Load save
Right shift: Change command

FUNCTIONS:
Cube: Creates a solid cube of blocks in a given area.
Hcube: Creates a hollow cube of blocks in a given area.
Sphere: Creates a solid sphere of blocks with a given radius. The center is at the player's legs. The player will be teleported out before they are trapped.
Hsphere: Creates a hollow sphere blocks with a given radius. The center is at the player's legs.
Walls: Creates walls around a given area.
Center: Creates a single block at the center of a given area.
Replace: Replaces certain blocks in a given area with a list of player chosen ID's and data. 
For example, if you want to replace all the grass and birch wood in the given area with TNT blocks with data 1 and gravel:
The query you will see:
Replace
Pos1:  0   1   -7
Pos2:  -8   3   1
How many types of blocks would you like to replace? 2
ID or Block to be replaced 1/2 grass
ID:  2
Data of Block to be replaced 1/2 0
ID or Block to be replaced 2/2 wood
ID:  17
Data of Block to be replaced 2/2 2
How many different blocks would you like to replace them with? 2
ID or Block to be replaced 1/2 tnt
ID:  46
Data of Block to be replaced 1/2 1
ID or Block to be replaced 2/2 gravel
ID:  13
Data of Block to be replaced 2/2 0
Replacenear: Same thing, only you give it a radius. Note that this will scan every single air block, and could take a while.

Thanks for downloading, and if there is any features you would like added, feel free to tell me!
Please report any bugs.

Known bugs:
Replace and replacenear cannot do multiple blocks with different data.