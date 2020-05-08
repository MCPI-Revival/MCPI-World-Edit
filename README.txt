# MCPI-World-Edit
To download older versions, go to the releases tab
An extremely simple version of world edit for MCPI.
Up arrow: Toggle between Void, Small Superflat, and Large Superflat Worlds.
The first time you do it, there will be a lot of lag.
Left arrow: Select Position 1
Right arrow: Select Position 2
Down arrow: Fill in with blocks
Right shift: Change Function
You will be prompted to give a block ID and block Data in the terminal or IDLE shell depending on where you are
running it from.
Type 0 for block data if you don't know what it is.
For a full list of block ID's, see this website:
https://www.raspberrypi-spy.co.uk/2014/09/raspberry-pi-minecraft-block-id-number-reference/
HOW TO DOWNLOAD AND USE:
This version is a pretty limited version of the WorldEdit mod for Minecraft Java Edition.
This is made for use on the Raspberry Pi, and will work on any model.
You need to have Python 3.7 installed on your pi as well as Minecraft Pi itself to be able to run this program.
How To Install:
Open terminal
Type "pip3 install pynput" (Without the quotes)
If you don't have IDLE installed, I recommend that you install it with the command:
 "sudo apt-get install idle-python3.7" (Without quotes)
You should see IDLE appear in your programming menu. Launch it and open the mod (File, Open), then hit "Run" and then "Run Module"
Make sure that Minecraft Pi is open first.
If you don't want to install IDLE, you can launch the mod from terminal or Thonny python IDE.
First, navigate to where the file is stored. It will probably be in your downloads folder. If so, type:
"cd /home/pi/Downloads"
Then to launch the program:
"python MCPI-WorldEdit-V0.1A.py" (change the version number if you're using a different one)
Make sure to launch Minecraft Pi first before running the program.
