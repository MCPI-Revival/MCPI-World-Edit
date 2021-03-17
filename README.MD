# MCPI-World-Edit
A extremely simple version of worldedit for MCPI, which functions such as shape generation, world type changing, and even "schmatics"! Made by [scratchermatch](https://github.com/scratchermatch). (some revisions made by [Robert Furr](https://github.com/robtech21))

## SETUP
1) Download the python script at https://github.com/MCPI-Revival/MCPI-World-Edit/releases/latest. In terminal, type `pip3 install -r requirements.txt` and wait for it to finish.
2) Make sure that minecraft is open and a world is loaded. Open the python script in a code IDE, or run it with `python3 MCPI_World_Edit*`
3) You can also run it by opening your terminal and typing `chmod +x MCPI_World_Edit` (you only need to do that once) and run it by typing `./MCPI_World_Edit*` 

Due to the nature of MCPI multiplayer, things created using the python api will not be seen by others on a server.
Only things created by the host are universal (so don't go on a server building giant objects because only you'll be able to see them!).

## COMMANDS
Up arrow: Toggle between Void, Small Superflat, and Large Superflat Worlds.
The first time you do it, there will be a lot of lag.
Left arrow: Select Position 1
Right arrow: Select Position 2
Down arrow: Run command
Right control: Save game
Right alt: Load save
Right shift: Change command

## FUNCTIONS
Cube: Creates a solid cube of blocks in a given area.
Hcube: Creates a hollow cube of blocks in a given area.
Sphere: Creates a solid sphere of blocks with a given radius. The center is at the player's legs. The player will be teleported out before they are trapped.
Hsphere: Creates a hollow sphere blocks with a given radius. The center is at the player's legs.
Walls: Creates walls around a given area.
Center: Creates a single block at the center of a given area.
Replace: Replaces certain blocks in a given area with a list of player chosen ID's and data. 
For example, if you want to replace all the grass and birch wood in the given area with TNT blocks with data 1 and gravel:
The query you will see:
- Replace
- Pos1:  0   1   -7
- Pos2:  -8   3   1
- How many types of blocks would you like to replace? 2
- ID or Block to be replaced 1/2 grass
- ID:  2
- Data of Block to be replaced 1/2 0
- ID or Block to be replaced 2/2 wood
- ID:  17
- Data of Block to be replaced 2/2 2
- How many different blocks would you like to replace them with? 2
- ID or Block to be replaced 1/2 tnt
- ID:  46
- Data of Block to be replaced 1/2 1
- ID or Block to be replaced 2/2 gravel
- ID:  13
- Data of Block to be replaced 2/2 0

Go to [our wiki](https://wiki.mcpirevival.tk/wiki/Minecraft:_Pi_Edition_block_list) for a full block ID reference!

Replacenear: Same thing, only you give it a radius. Note that this will scan every single air block, and could take a while.

Thanks for downloading, and if there are any features you would like added, feel free to tell me!
Please report any bugs.

Known bugs:
Replace and replacenear cannot do multiple blocks with different data.
