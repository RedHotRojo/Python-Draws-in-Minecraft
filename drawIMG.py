from PIL import Image
import difflib
import keyboard
import numpy as np
import ast
from time import sleep as delay
img = Image.open("C:\\Users\\Rohit\\Pictures\\billmurrayasgeorgemasonsquare.jpg").convert("RGBA")
loaded = img.load()
width, height = img.size
f = open(f"C:\\Users\\Rohit\\Documents\\21w16a_textures\\allBlocks.txt", 'r')
file = f.read()
f.close()
clrs = [ast.literal_eval(x[:(x.index(';'))]) if x[0] == '[' else None for x in file.split(':')]
clrs.pop(0)
clrs = np.array(clrs, dtype=float)
names = [x for x in file.split(';')]
names.remove('')
names = [x[:x.index(':')] for x in names]
keyboard.wait('j')
knownClrs = {}
for i in range(width*height):
    if keyboard.is_pressed('shift'):
        print("user exit")
        break
    if keyboard.is_pressed('ctrl'):
        delay(5)
        keyboard.wait('ctrl')
    clr = loaded[width-1-i%width, height-1-int(i/width)]
    block = None
    if str(clr) in knownClrs:
        block = knownClrs[str(clr)]
    else:
        distances = np.sqrt(np.sum((clrs-np.array([clr[0], clr[1], clr[2]], dtype=float))**2,axis=1))
        block = names[np.where(distances==np.amin(distances))[0][0]]
        knownClrs[str(clr)] = block
    keyboard.press_and_release("/")
    delay(0.05)
    keyboard.write(f"setblock {width-1-i%width} 1 {int(i/width)+260} {block}")
    keyboard.press_and_release("Enter")
    delay(0.05)