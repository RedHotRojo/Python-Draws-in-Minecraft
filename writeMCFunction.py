# Please open an Issue if you wish for this file to be heavily commented
from PIL import Image
import numpy as np
import ast
FILE_NAME = "FILE_NAME"
img = Image.open(f"C:\\Users\\YOUR_NAME\\Pictures\\{FILE_NAME}.jpg").convert("RGBA")
loaded = img.load()
width, height = img.size
f = open("C:\\Users\\YOUR_NAME\\Documents\\GitHub\\Python-Draws-in-Minecraft\\allBlocks.txt", 'r')
file = f.read()
f.close()
clrs = [ast.literal_eval(x[:(x.index(';'))]) if x[0] == '[' else None for x in file.split(':')]
clrs.pop(0)
clrs = np.array(clrs, dtype=float)
names = [x for x in file.split(';')]
names.remove('')
names = [x[:x.index(':')] for x in names]
knownClrs = {}
functionFile = open(f"C:\\Users\\YOUR_NAME\\AppData\\Roaming\\.minecraft\\saves\\WORLD_NAME\\datapacks\\drawimage\\data\\draw\\functions\\{FILE_NAME}.mcfunction", 'w')
fileNum = 0
doCreateCanvas = None
while doCreateCanvas != 0 and doCreateCanvas != 1:
    try:
        doCreateCanvas = int(input("Do you want the mcfunction for creating the canvas? (Enter 0 for no, 1 for yes) "))
    except:
        doCreateCanvas = int(input("Enter 0 for no, 1 for yes! "))
if doCreateCanvas:
    print(f"Creating a grassy canvas from 0 0 0 to {width-1} 0 {height-1}")
    canvasFile = open(f"C:\\Users\\YOUR_NAME\\AppData\\Roaming\\.minecraft\\saves\\WORLD_NAME\\datapacks\\drawimage\\data\\draw\\functions\\create_canvas_for_{FILE_NAME}.mcfunction", 'w')
    lastZ = 0
    step = 32768 // width - 1
    thisZ = step
    while thisZ < height-1:
        canvasFile.write(f"fill 0 0 {lastZ} {width-1} 0 {thisZ} grass_block\n")
        canvasFile.write(f"fill 0 1 {lastZ} {width-1} 1 {thisZ} air\n")
        lastZ = thisZ + 1
        thisZ += step if thisZ < height else height-1
    canvasFile.write(f"fill 0 0 {lastZ} {width-1} 0 {height-1} grass_block\n")
    canvasFile.write(f"fill 0 1 {lastZ} {width-1} 1 {height-1} air\n")
for i in range(width*height):
    clr = loaded[width-1-i%width, height-1-int(i/width)]
    block = None
    if str(clr) in knownClrs:
        block = knownClrs[str(clr)]
    else:
        distances = np.sqrt(np.sum((clrs-np.array([clr[0], clr[1], clr[2]], dtype=float))**2,axis=1))
        block = names[np.where(distances==np.amin(distances))[0][0]]
        knownClrs[str(clr)] = block
    functionFile.write(f"setblock {width-1-i%width} 1 {int(i/width)} {block}")
    if i%65535 == 0 and i > 0:
        functionFile.close()
        functionFile = open(f"C:\\Users\\YOUR_NAME\\AppData\\Roaming\\.minecraft\\saves\\WORLD_NAME\\datapacks\\drawimage\\data\\draw\\functions\\{FILE_NAME}{fileNum}.mcfunction", 'w')
        fileNum += 1
    elif i != width*height-1: functionFile.write('\n')
functionFile.close()
print(f"Don't forget! Create a grassy area by {width}, {height}!" if not doCreateCanvas else f"Don't forget to run /function draw:create_canvas_for_{FILE_NAME}!")
input()