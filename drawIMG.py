# Only tested in Windows
from PIL import Image # pip install pillow
import keyboard # pip install keyboard
import numpy as np # pip install numpy
import ast # built-in
from time import sleep # built-in
img = Image.open("C:\\Users\\YOUR_USER_NAME\\Pictures\\YOUR_IMAGE.FILE_EXTENSION").convert("RGBA") # Change to the directory, file name, and file extension of your image. Don't forget to escape the backslashes!
loaded = img.load() # Contains pixels
width, height = img.size # easy access
f = open(f"C:\\Users\\YOUR_USER_NAME\\Documents\\21w16a_textures\\allBlocks.txt", 'r') # That's where I have the document; Change the directory to yours, of course
file = f.read() # Get all contents
f.close() # and then close it quickly
clrs = [ast.literal_eval(x[:(x.index(';'))]) if x[0] == '[' else None for x in file.split(':')] # Get the colors only as a list
clrs.pop(0) # The first element is usually empty
clrs = np.array(clrs, dtype=float) # numpy array
names = [x for x in file.split(';')] # Split each blocks and it's color; getting the names is a bit harder
names.remove('') # The last element is usually empty
names = [x[:x.index(':')] for x in names] # Get the names only as a list; numpy array is not required
"""
Having the space ready:
Make sure you have matched the space to be drawn on to the code
Have a layer of any block underneath so that blocks like sand don't fall
Keep Minecraft open, press F1 and close F3 if necessary 
Make sure you won't be needing this computer for a few hours
If you do end up needing the computer in the middle of drawing, you can pause the drawing pressing and holding CTRL
Press CTRL to resume the drawing -- NOTE: you will likely need CTRL for everyday use. Therefore, note the last i printed after pressing CTRL. Then, add the line if i > the i you wrote down inside of the for loop around all of the code and properly indent. Then, rerun the program
If you know that you will not be able to resume drawing, you can also press and hold SHIFT to exit this program quickly.
"""
keyboard.wait('j') # When you're ready to draw, press j on your keyboard
knownClrs = {} # Store colors that have already been calculated to quickly access them again later
for i in range(width*height):
    if keyboard.is_pressed('shift'): # If the program should be closed; press and hold.
        print("user exit") # If you accidentally pressed shift, you'll figure out what happened here.
        break
    if keyboard.is_pressed('ctrl'): # Pause the program
        print(i)
        sleep(5)
        keyboard.wait('ctrl')
    clr = loaded[width-1-i%width, height-1-int(i/width)] # Get the current pixel's color
    block = None # The block name
    if str(clr) in knownClrs: # This color has already been calculated
        block = knownClrs[str(clr)]
    else:
        distances = np.sqrt(np.sum((clrs-np.array([clr[0], clr[1], clr[2]], dtype=float))**2,axis=1)) # Algorithm I didn't create nor do I understand 
        block = names[np.where(distances==np.amin(distances))[0][0]] # Algorithm I didn't create; [0][0] gets the index from the numpy array and uses it for names[]
        knownClrs[str(clr)] = block # This color was calculated for the first time; store it for future reference
    keyboard.press_and_release("/") # Start writing a command in Minecraft
    sleep(0.05) # Without this, Minecraft writes a double slash or doesn't write the command at all
    keyboard.write(f"setblock {width-1-i%width} 1 {int(i/width)} {block}") # Write the command using the current positioning and block
    keyboard.press_and_release("Enter") # Run the command
    sleep(0.001)# Quick cooldown; Minecraft will skip several blocks without this or not run the command at all; may require increasing if Minecraft is still skipping blocks
